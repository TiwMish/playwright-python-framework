from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_successful_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    InventoryPage(page).expect_loaded()


def test_locked_out_user_shows_error(page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user", "secret_sauce")
    login.expect_error("Epic sadface: Sorry, this user has been locked out.")
