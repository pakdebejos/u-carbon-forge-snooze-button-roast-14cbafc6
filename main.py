"""Pressing You Nine Times Is: one-line entry for make.fun.

The program writes exactly one line - the drafted winning line for the 'Snooze Button Roast' bounty - to entry.txt in the
output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader). The line is a fixed constant with no trailing newline, so both of the grader's runs
write byte-identical output: 112 UTF-8 characters, inside the 1-200 gate.
"""
import os

LINE = 'Pressing you nine times is not rest, it is a subscription to disappointment that bills me every morning at 6 AM.'

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
