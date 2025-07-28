import os
import json
from pathlib import Path
from utils.pdf_extractor import extract_pdf_data

def process_pdfs():
    # Directories
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Find all PDFs in input directory
    pdf_files = list(input_dir.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found in input folder.")
        return

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        result = extract_pdf_data(pdf_file)

        # Save JSON output in the correct schema
        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        print(f"Generated: {output_file.name}")

if __name__ == "__main__":
    print("Starting processing PDFs...")
    process_pdfs()
    print("Processing completed. Results saved in output/")
