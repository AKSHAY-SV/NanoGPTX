from pathlib import Path
import fitz  # PyMuPDF
from tqdm import tqdm


RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")


def extract_pdf(pdf_path: Path) -> str:
    """Extract all text from a PDF file."""

    document = fitz.open(pdf_path)
    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def main():

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    pdf_files = sorted(RAW_DIR.rglob("*.pdf"))

    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"\nFound {len(pdf_files)} PDF(s).\n")

    for pdf in tqdm(pdf_files):

        text = extract_pdf(pdf)

        output_file = PROCESSED_DIR / f"{pdf.stem}.txt"

        output_file.write_text(text, encoding="utf-8")

    print("\n✅ Extraction Complete!")


if __name__ == "__main__":
    main()
