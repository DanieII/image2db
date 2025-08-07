import pytesseract


class TextExtractor:
    def __init__(self, language: str):
        self.language = language

    def extract(self, image_path: str) -> str:
        return pytesseract.image_to_string(image_path, lang=self.language)
