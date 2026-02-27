# Testautomation — Individuellt Projektarbete
FSH | Shamim Russell

Automatiska tester för Söderbröder Finans AB:s låneportal.

- **API:** https://souderbroder-loan-lab.lovable.app/api-docs
- **Webb-GUI:** https://souderbroder-loan-lab.lovable.app

---

## Installation

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

Skapa en `.env`-fil i roten med dina API-nycklar.

---

## Köra tester

```bash
pytest -v                           # Alla tester
pytest tests/api/ -v                # API-tester
pytest tests/gui/ -v --headed       # GUI-tester
k6 run .\k6\sb.js                   # Prestandatest API
k6 run .\k6\browser_test_studio.js  # Prestandatest GUI
```

---

## Projektstruktur

```
src/
  helpers/loan_client.py   # API-klient
  pages/                   # Page Object Model (4 sidor)
tests/
  api/                     # API-tester (tekniska + affär)
  gui/                     # Playwright GUI-tester
  test_data.py             # Faker + Skatteverkets testpersonnummer
k6/                        # Prestandatester
```

---

## Tekniker
Pytest · Playwright · Requests · Faker · k6 · k6 Studio