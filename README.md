# playwright-python-framework

Python + pytest + Playwright framework for demo web + API testing — a portfolio project by Isha Tiwari, Lead SDET, Toronto.

## What is in here
- **Page objects:** `pages/login_page.py`, `inventory_page.py`, `cart_page.py`, `checkout_page.py`
- **UI tests (3):** successful login, locked-out user error, and a full add-to-cart → checkout → order-complete flow on SauceDemo (public demo site)
- **API tests (3):** get post, create post (201), and missing post (404) against a public demo API
- **Fixtures:** one browser per session, one isolated context per test, so tests never share cookies or cart state
- **CI:** GitHub Actions workflow that installs Python + Playwright and runs `pytest`

## Stack
Python, pytest, Playwright (Python), Page Object Model, role-based locators (`get_by_role` / `get_by_placeholder`), auto-waiting `expect()` assertions, GitHub Actions.

## Run locally
```
python -m venv .venv
pip install -r requirements.txt
playwright install chromium
pytest
```

## Design notes
- No UI login in every test by default: login tests cover login itself; for a larger suite, log in once via API and reuse `storage_state`.
- No `time.sleep` — auto-waiting assertions handle dynamic pages, and flaky tests are debugged with the trace viewer, not retries as a fix.
- Thin UI layer on top of API coverage, following the test pyramid.

No proprietary code from previous employers is included. Demo sites/APIs only.
