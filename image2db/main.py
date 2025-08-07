import argparse
import os
from dotenv import load_dotenv
from inserter import SupabaseInserter
from processor import Image2DB


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
SUPABASE_URL = os.getenv("SUPABASE_URL", "")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")


def main():
    parser = argparse.ArgumentParser(description="Extract text from an image")
    parser.add_argument("image_path", type=str, help="Path to the image file")
    args = parser.parse_args()

    inserter = SupabaseInserter(url=SUPABASE_URL, key=SUPABASE_KEY)
    processor = Image2DB(
        openai_api_key=OPENAI_API_KEY,
        inserter=inserter,
        ocr_language="bul",
        model="gpt-4o-mini",
    )
    result = processor.process(image_path=args.image_path)

    print(result)


if __name__ == "__main__":
    main()
