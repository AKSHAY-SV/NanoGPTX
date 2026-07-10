from pathlib import Path

INPUT_DIR = Path("data/final")
OUTPUT_FILE = Path("data/final/dataset.txt")


def main():

    txt_files = sorted(INPUT_DIR.glob("*.txt"))

    with OUTPUT_FILE.open("w", encoding="utf-8") as outfile:

        for txt in txt_files:

            outfile.write(f"\n\n===== {txt.stem} =====\n\n")

            outfile.write(txt.read_text(encoding="utf-8"))

            outfile.write("\n")

    print(f"\nMerged {len(txt_files)} files.")
    print(f"Dataset saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
