# utils/heading_rules.py

# Keywords to boost heading confidence
keywords = ["introduction", "abstract", "summary", "conclusion"]

def detect_heading_level(text, font_size, bold, italic):
    """
    Advanced heading detection with confidence scoring.
    Combines font size, style, and keyword presence.
    """
    confidence = 0.0
    level = None

    # Font size heuristic
    if font_size >= 14:
        level = "H1"
        confidence += 0.5
    elif font_size >= 12:
        level = "H2"
        confidence += 0.3
    elif font_size >= 10:
        level = "H3"
        confidence += 0.2

    # Bold/Italic adds confidence
    if bold:
        confidence += 0.2
    if italic:
        confidence += 0.1

    # Keyword match
    for kw in keywords:
        if kw.lower() in text.lower():
            confidence += 0.2

    return (level, confidence) if confidence >= 0.3 else (None, 0.0)


def determine_heading_level(font_size, bold=False):
    """
    Simple fallback rule based on font size.
    """
    if font_size >= 18:
        return "H1"
    elif font_size >= 16:
        return "H2"
    elif font_size >= 14:
        return "H3"
    elif font_size >= 12:
        return "H4"
    return None
