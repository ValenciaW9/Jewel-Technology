# Jewel.Technology 💎-OpenQQuantify Jewelery Website

An AI-powered jewelry discovery platform using Flask, OpenAI, and 3D assets.

## Features
- Flask backend API with OpenAI integration
- SQLite jewelry product database
- Interactive frontend with real-time AI chat
- 3D jewelry previews (Three.js)

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/ingest.py
python app.py

pip install flask stripe

npm run dev

pip install flask flask_sqlalchemy flask_login flask_security-too flask_mail gunicorn


export STRIPE_SECRET_KEY=sk_test_...
export STRIPE_PUBLISHABLE_KEY=pk_test_...





export STRIPE_SECRET_KEY=""

export STRIPE_PUBLISHABLE_KEY=""



STRIPE_PUBLISHABLE_KEY:



STRIPE_SECRET_KEY


### `docs/datasets.md`
```md
# Datasets Used

| Dataset Source | Type | License |
|----------------|------|---------|
| Kaggle Jewelry Dataset | CSV (price, material, etc.) | CC-BY 4.0 |
| OpenCorporates | Company Metadata | Share-Alike |
| OpenStreetMap | Store Geolocation | ODbL |
