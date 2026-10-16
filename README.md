# AURIX-TECH NATION

A responsive starter website built with Python Flask for the AURIX-TECH NATION brand.

## Features
- Responsive homepage
- Course listing and individual course detail pages
- AURIX bot centre with pairing/Telegram links
- Digital services listing
- Contact page with basic form validation
- About page
- Shared navigation, mobile menu, and footer

## Run locally

Python 3.10+ is recommended.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux/Termux:
source .venv/bin/activate

pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Deploy to Render
1. Upload this project to a GitHub repository.
2. In Render, create a **New Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Add an environment variable named `SECRET_KEY` with a long random value.
6. Deploy and test every page and link.

## Before production
- The contact form currently validates and logs basic enquiry metadata; it does **not** email or save messages. Connect a mail provider or database.
- Add CSRF protection, rate limiting, privacy notice, and a proper contact-storage/notification workflow.
- Add admin authentication before adding any dashboard that changes site content.
- Keep secrets and API keys in environment variables, never in source control.
- Confirm course prices, schedules, and service terms before publishing.
- Use a custom domain only after checking availability and configuring DNS.

## Main structure
- `app.py`: Flask routes and content data
- `templates/`: HTML pages
- `static/css/style.css`: responsive styles
- `static/js/main.js`: mobile navigation and small interactions
