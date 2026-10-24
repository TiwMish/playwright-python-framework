from playwright.sync_api import expect, Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.cart_link = page.locator("[data-test='shopping-cart-link']")

    def expect_loaded(self):
        expect(self.title).to_have_text("Products")
        expect(self.page.locator(".inventory_item").first).to_be_visible()

    def add_to_cart(self, product_slug: str):
        # SauceDemo exposes stable data-test ids, e.g.
        # add-to-cart-sauce-labs-backpack. Prefer those over brittle CSS.
        self.page.locator(f"[data-test='add-to-cart-{product_slug}']").click()

    def open_cart(self):
        self.cart_link.click()
