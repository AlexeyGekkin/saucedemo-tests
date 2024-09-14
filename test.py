from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.saucedemo.com/"


def find_element(driver, by, value):
    """Function to find an element on the page"""
    try:
        return driver.find_element(by, value)
    except NoSuchElementException:
        assert False, f"Element with {by}='{value}' not found"


def login(driver, username, password, url=BASE_URL):
    """Login function"""
    driver.get(url)
    find_element(driver, By.ID, "user-name").send_keys(username)
    find_element(driver, By.ID, "password").send_keys(password)
    find_element(driver, By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Login error"
    print("Login successful")


def add_item_to_cart(driver, item_id):
    """Add item to cart function"""
    find_element(driver, By.ID, item_id).click()

    # Navigate to cart
    find_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url, "Error navigating to cart"

    # Check item in cart
    item_in_cart = find_element(driver, By.CLASS_NAME, "inventory_item_name")
    assert item_in_cart is not None, "Item not added to cart"
    print(f"Item '{item_in_cart.text}' successfully added to cart")


def checkout(driver, first_name, last_name, postal_code):
    """Checkout function"""
    find_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    find_element(driver, By.ID, "checkout").click()
    find_element(driver, By.ID, "first-name").send_keys(first_name)
    find_element(driver, By.ID, "last-name").send_keys(last_name)
    find_element(driver, By.ID, "postal-code").send_keys(postal_code)
    find_element(driver, By.ID, "continue").click()
    find_element(driver, By.ID, "finish").click()
    assert "checkout-complete.html" in driver.current_url, (
        "Error completing purchase"
    )
    print("Purchase successfully completed")


def run_test():
    """Main test function"""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    try:
        login(driver, "standard_user", "secret_sauce")
        add_item_to_cart(driver, "add-to-cart-sauce-labs-backpack")
        checkout(driver, "Alex", "Gek", "123123")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test()
