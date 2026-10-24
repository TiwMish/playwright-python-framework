from playwright.sync_api import expect, Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.checkout_button = page.locator("[data-test='checkout']")

    def expect_item(self, name: str):
        expect(self.page.locator(".inventory_item_name", has_text=name)).to_be_visible()

    def checkout(self):
        self.checkout_button.click()
