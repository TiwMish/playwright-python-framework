from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_add_to_cart_and_checkout(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(page)
    inventory.expect_loaded()
    inventory.add_to_cart("sauce-labs-backpack")
    inventory.open_cart()

    cart = CartPage(page)
    cart.expect_item("Sauce Labs Backpack")
    cart.checkout()

    checkout = CheckoutPage(page)
    checkout.fill_details("Isha", "Test", "M5V 1J1")
    checkout.finish()
    checkout.expect_complete()
