# utils/pdf_extractor.py

import fitz  # PyMuPDF
from utils.heading_rules import detect_heading_level, determine_heading_level
from utils.language_detector import detect_language

def extract_pdf_data(pdf_path):
    """
    Extract headings, confidence, language, and page numbers from the entire PDF.
    """
    headings = []
    title_candidate = {"text": "", "font_size": 0}

    doc = fitz.open(pdf_path)

    for page_num, page in enumerate(doc):  # 0-indexed
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                font_size = 0
                bold = False
                italic = False

                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    line_text += text + " "
                    font_size = span["size"]
                    font_name = span.get("font", "").lower()
                    bold = bold or ("bold" in font_name)
                    italic = italic or ("italic" in font_name)

                line_text = line_text.strip()
                if not line_text:
                    continue

                # Detect heading using advanced method
                level, confidence = detect_heading_level(line_text, font_size, bold, italic)

                # Fallback if confidence low
                if not level:
                    level = determine_heading_level(font_size, bold)

                if level:
                    language = detect_language(line_text)
                    headings.append({
                        "level": level,
                        "text": line_text,
                        "page": page_num,
                        "language": language,
                        "confidence": round(confidence, 2)
                    })

                    # Track the largest font title candidate
                    if font_size > title_candidate["font_size"]:
                        title_candidate = {"text": line_text, "font_size": font_size}

    doc.close()

    return {
        "title": title_candidate["text"],
        "outline": headings
    }
