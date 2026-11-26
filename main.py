"""Write the out-of-office auto-reply to /output/entry.txt.

Reads the output directory from MAKEFUN_OUTPUT_DIR when set, else /output.
"""

from pathlib import Path
import os

LINE = "I'm out of the office until Monday; my inbox is a 400-email avalanche I'll be shovelling through for days, so please expect a slow reply — thank you for your patience."

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
