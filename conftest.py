"""Shared Playwright fixtures.

Design choices worth noting in an interview:
- One browser per session, one isolated context per test. Tests never
  share cookies, storage, or cart state, so they can run in parallel.
- No UI login in every test by default here: the login tests cover login
  itself, and the cart tests log in through the page object once per test.
  For a larger suite, log in once via API and reuse storage_state instead.
"""

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def api_context(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield context
    context.dispose()
