# utils/language_detector.py

from langdetect import detect

def detect_language(text):
    """
    Detect language of given text using langdetect.
    Handles multilingual cases like Japanese, French, etc.
    """
    try:
        if len(text.strip()) < 2:
            return "unknown"
        return detect(text)
    except:
        return "unknown"
