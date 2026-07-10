from pathlib import Path
import re

INPUT_DIR = Path("data/processed")
OUTPUT_DIR = Path("data/final")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def clean_text(text: str) -> str:
    """Basic text cleaning."""

    # Normalize line endings
    text = text.replace("\r\n", "\n")

    # Remove tabs
    text = text.replace("\t", " ")

    # Collapse multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Strip leading/trailing whitespace
    text = text.strip()

    return text


def main():

    txt_files = sorted(INPUT_DIR.glob("*.txt"))

    print(f"Cleaning {len(txt_files)} file(s)...\n")

    for txt in txt_files:

        text = txt.read_text(encoding="utf-8")

        cleaned = clean_text(text)

        output = OUTPUT_DIR / txt.name

        output.write_text(cleaned, encoding="utf-8")

        print(f"✔ {txt.name}")


if __name__ == "__main__":
    main()
