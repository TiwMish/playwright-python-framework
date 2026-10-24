# playwright-python-framework

Python + pytest + Playwright framework for demo web + API testing — built as a recruiter-ready portfolio project by Isha Tiwari, Lead SDET, Toronto.

## Stack
- Python, pytest, Playwright (Python)
- Page Object Model, fixtures in conftest.py
- API testing via Playwright APIRequestContext + requests-style assertions
- Role-based locators only (get_by_role / label / text / test_id), auto-waiting expect() assertions
- GitHub Actions CI, HTML + trace reporting on failure

## Structure (planned)
```
pages/            # Page objects: login, products, cart/checkout
tests/
  ui/             # End-to-end UI flows
  api/            # API + UI combined flows
conftest.py       # Browser/context fixtures, storage-state login
pytest.ini        # Markers, test discovery
.github/workflows/ci.yml
```

## Run
```
python -m venv .venv
pip install pytest playwright
playwright install chromium
pytest
```

## What this demonstrates
- No UI login in every test: API login once, reuse storage state
- Independent tests with unique test data, no shared cart/order state
- Flaky-test debugging via trace viewer, not sleeps or retries as a fix
- Thin UI layer on top of API coverage, following the test pyramid

No proprietary code from previous employers is included. Demo sites/APIs only.
