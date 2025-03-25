# Color Analyzer

This Python project analyzes a list of colors, finds the brightest one, and determines its closest named color using an API from `www.csscolorsapi.com`.

## 📌 Features
- Computes brightness of hex colors.
- Finds the brightest color from a list.
- Matches the brightest color to the closest color name from `www.csscolorsapi.com` using eucledean distance.

## Setup and Run

- install: `pip install -r requirements.txt`
- test:`pytest tests/`
- run: `python main.py`

### Create a virtual environment to manage dependencies:
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
pip install -r requirements.txt

