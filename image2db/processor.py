from extractor import TextExtractor
from parser import TextParser
from inserter import DatabaseInserter


class Image2DB:
    def __init__(
        self,
        openai_api_key: str,
        inserter: DatabaseInserter,
        ocr_language: str,
        model: str,
    ):
        self.extractor = TextExtractor(language=ocr_language)
        self.parser = TextParser(api_key=openai_api_key, model=model)
        self.inserter = inserter

    def process(self, image_path: str):
        text = self.extractor.extract(image_path)
        data = self.parser.parse(text)
        result = self.inserter.insert(data)

        return result
