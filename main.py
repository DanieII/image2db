import argparse
import os
from dotenv import load_dotenv
import pytesseract
import openai

IMAGE_LANGUAGE = "bul"

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


def get_text_from_image(image_path):
    return pytesseract.image_to_string(image_path, lang=IMAGE_LANGUAGE)


def get_structured_data(text):
    pass


def main():
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()

    text = get_text_from_image(args.image_path)


if __name__ == "__main__":
    main()
