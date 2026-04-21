"""Strip personal/machine paths out of committed notebooks.

When an Agent executes notebooks locally (via `jupyter nbconvert --execute`),
stderr warnings from third-party libraries (tqdm, scipy, transformers, ...) can
embed **absolute paths** like `/Users/someone/opt/anaconda3/...` into the
notebook's stored outputs. Those paths are:

  1. personally identifying, and
  2. useless to other readers.

This script walks every `.ipynb` under the given root and rewrites outputs so
that:

  * `stream.stderr` outputs that contain any `/Users/...` path are **dropped**
    entirely (they are noise, not signal).
  * `stream.stdout` and rich-data outputs have `/Users/<user>` substituted for
    `/Users/<any-username>` — preserves the shape of the output without leaking
    identity.
  * `error.traceback` entries are regex-scrubbed in place so the traceback
    remains readable but no longer names a user.

Safe to run repeatedly: the operation is idempotent.

Usage:
    python utils/scrub_notebooks.py                 # scrub everything under notebooks/
    python utils/scrub_notebooks.py path/to/file.ipynb
    python utils/scrub_notebooks.py --check         # exit 1 if any sensitive path remains
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

# `/Users/<word-chars>` catches macOS usernames. Extend here if you also need to
# scrub `/home/...` (Linux) or `C:\Users\...` (Windows).
USER_PATH_RE = re.compile(r"/Users/[A-Za-z0-9_.-]+")

# An arbitrary placeholder that is still clearly a path but carries no identity.
PLACEHOLDER = "/Users/<user>"


def scrub_text(txt: str) -> str:
    return USER_PATH_RE.sub(PLACEHOLDER, txt)


def clean_outputs(outputs: list[dict]) -> list[dict]:
    cleaned: list[dict] = []
    for out in outputs:
        otype = out.get("output_type")

        # 1. stderr stream: drop the chunk if it leaks a path, scrub otherwise.
        if otype == "stream" and out.get("name") == "stderr":
            text = "".join(out.get("text", []))
            if USER_PATH_RE.search(text):
                # Drop the output entirely — these are environment warnings.
                continue
            out["text"] = scrub_text(text).splitlines(keepends=True)
            cleaned.append(out)
            continue

        # 2. error tracebacks: scrub in place.
        if otype == "error":
            out["traceback"] = [scrub_text(line) for line in out.get("traceback", [])]
            cleaned.append(out)
            continue

        # 3. stdout stream: scrub in place.
        if otype == "stream":
            out["text"] = [scrub_text(s) for s in out.get("text", [])]

        # 4. rich-data outputs (display_data, execute_result): scrub string mimes.
        if "data" in out:
            for mime, v in list(out["data"].items()):
                if isinstance(v, str):
                    out["data"][mime] = scrub_text(v)
                elif isinstance(v, list) and v and isinstance(v[0], str):
                    out["data"][mime] = [scrub_text(s) for s in v]

        cleaned.append(out)
    return cleaned


def scrub_notebook(path: pathlib.Path) -> bool:
    """Scrub one notebook. Returns True if the file changed."""
    raw = path.read_text(encoding="utf-8")
    # Quick bail-out: nothing to do.
    if "/Users/" not in raw:
        return False

    nb = json.loads(raw)
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        cell["outputs"] = clean_outputs(cell.get("outputs", []))

    new_raw = json.dumps(nb, ensure_ascii=False, indent=1)
    if new_raw == raw:
        return False
    path.write_text(new_raw, encoding="utf-8")
    return True


def collect_notebooks(targets: list[str]) -> list[pathlib.Path]:
    paths: list[pathlib.Path] = []
    for t in targets:
        p = pathlib.Path(t)
        if p.is_dir():
            paths.extend(p.rglob("*.ipynb"))
        elif p.suffix == ".ipynb":
            paths.append(p)
    # Skip jupyter autosave folders — they get regenerated anyway.
    return [p for p in paths if ".ipynb_checkpoints" not in p.parts]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("paths", nargs="*", default=["notebooks"],
                        help="Notebook files or folders to scrub (default: notebooks/)")
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if any /Users/ path is found; do not modify files.")
    args = parser.parse_args()

    targets = collect_notebooks(args.paths)
    if not targets:
        print("No notebooks found under:", args.paths)
        return 0

    if args.check:
        offenders = [str(p) for p in targets if "/Users/" in p.read_text(encoding="utf-8")]
        if offenders:
            print("Sensitive paths remain in:")
            for p in offenders:
                print("  -", p)
            return 1
        print("OK - no /Users/ paths found in", len(targets), "notebooks.")
        return 0

    n_changed = 0
    for p in targets:
        if scrub_notebook(p):
            print("scrubbed", p)
            n_changed += 1
    print(f"\n{n_changed} of {len(targets)} notebook(s) modified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
