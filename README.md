import os
from pathlib import Path
from utils.pdf_extractor import extract_pdf_data
from utils.heading_rules import build_outline
from utils.json_writer import save_json

INPUT_DIR = Path("/app/input")
OUTPUT_DIR = Path("/app/output")

def process_pdfs():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pdf_files = list(INPUT_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDFs found in input directory.")
        return

    print("Processing started...")
    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        data = extract_pdf_data(pdf_file)
        outline = build_outline(data)
        result = {
            "title": outline.get("title", ""),
            "outline": outline.get("outline", [])
        }
        save_json(result, OUTPUT_DIR / f"{pdf_file.stem}.json")
    print("Processing completed. Results saved in output/")

if __name__ == "__main__":
    process_pdfs()
