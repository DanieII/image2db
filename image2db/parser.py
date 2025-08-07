from models import Records
from openai import OpenAI


class TextParser:
    def __init__(self, api_key: str, model: str):
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def parse(self, text: str) -> Records:
        response = self.client.responses.parse(
            model=self.model,
            input=[
                {
                    "role": "system",
                    "content": "Extract the information from the given text. Your response will be used in an automated system for inserting data into a database.",
                },
                {"role": "user", "content": text},
            ],
            text_format=Records,
        )

        if not response.output_parsed:
            raise ValueError("No data was extracted from the text")

        return response.output_parsed
