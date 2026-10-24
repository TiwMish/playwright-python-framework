from playwright.sync_api import expect, Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("[data-test='continue']")
        self.finish_button = page.locator("[data-test='finish']")
        self.complete_header = page.locator(".complete-header")

    def fill_details(self, first: str, last: str, postal: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postal)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()

    def expect_complete(self):
        expect(self.complete_header).to_have_text("Thank you for your order!")
