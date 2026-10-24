from playwright.sync_api import expect, Page


class LoginPage:
    """SauceDemo login page (public demo site, standard test users)."""

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error = page.locator("[data-test='error']")

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def expect_error(self, text: str):
        expect(self.error).to_contain_text(text)
