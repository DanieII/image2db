# image2db

image2db is an automation tool that lets you turn images into database records. Snap a photo (like a receipt or invoice), and it will read the text, figure out the important information with an OpenAI model, and insert them into your database.

---

## What does it do?

- 🖼️ **Reads images** with Tesseract OCR.
- 🧠 **Understands content** using OpenAI models (just tell it what fields you want!).
- 💾 **Saves the structured data** directly to your database — Supabase by default, but you can plug in whatever you need.
- 🛠️ **Customizable:** You decide what data to extract and where it should go.

---

## Getting Started

### 1. Install dependencies

```bash
git clone https://github.com/DanieII/image2db.git
cd image2db
pip install -r requirements.txt
```
You'll also need [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) installed.

---

### 2. Setup your environment

Copy `.env.example` to `.env` and fill in your keys:

```dotenv name=.env.example
OPENAI_API_KEY=

SUPABASE_URL=
SUPABASE_KEY=
```

---

### 3. Tell image2db what to extract and where to put it

- **Define your data model:**  
  Open `models.py` and fill out the `Record` class with the fields you care about.  
  _Example:_
  ```python
  class Record(BaseModel):
      invoice_number: str
      total: float
      date: str
  ```
- **Set up your database logic:**  
  Open `inserter.py` and make sure the `DatabaseInserter` (or `SupabaseInserter`) puts data into the right table, using the structure you defined.

---

## How do I use it?

Once you're set up, just run:

```bash
python3 main.py path/to/your/image.png
```

---

## Why?

I made this in a day to automate the boring task of typing up info from photos into a database. If you’re a developer who likes automating away repetitive chores (or just want to see LLMs and OCR work together), give it a try.

---

## License

MIT © 2025 Daniel Bogdanov

---

## Contributing

PRs and feedback are welcome!
