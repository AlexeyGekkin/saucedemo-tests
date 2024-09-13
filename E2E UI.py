from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "https://www.saucedemo.com/"


def find_element(driver, by, value):
    """Функция для поиска элемента на странице"""
    try:
        return driver.find_element(by, value)
    except NoSuchElementException:
        assert False, f"Элемент с {by}='{value}' не найден"


def login(driver, username, password, url=BASE_URL):
    """Функция авторизации"""
    driver.get(url)
    find_element(driver, By.ID, "user-name").send_keys(username)
    find_element(driver, By.ID, "password").send_keys(password)
    find_element(driver, By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url, "Ошибка авторизации"
    print("Авторизация прошла успешно")


def add_item_to_cart(driver, item_id):
    """Функция добавления товара в корзину"""
    find_element(driver, By.ID, item_id).click()

    # Переход в корзину
    find_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url, "Ошибка при переходе в корзину"

    # Проверка наличия товара в корзине
    item_in_cart = find_element(driver, By.CLASS_NAME, "inventory_item_name")
    assert item_in_cart is not None, "Товар не добавлен в корзину"
    print(f"Товар '{item_in_cart.text}' успешно добавлен в корзину")


def checkout(driver, first_name, last_name, postal_code):
    """Функция оформления заказа"""
    find_element(driver, By.CLASS_NAME, "shopping_cart_link").click()
    find_element(driver, By.ID, "checkout").click()
    find_element(driver, By.ID, "first-name").send_keys(first_name)
    find_element(driver, By.ID, "last-name").send_keys(last_name)
    find_element(driver, By.ID, "postal-code").send_keys(postal_code)
    find_element(driver, By.ID, "continue").click()
    find_element(driver, By.ID, "finish").click()
    assert "checkout-complete.html" in driver.current_url, (
        "Ошибка при завершении покупки"
    )
    print("Покупка успешно завершена")


def run_test():
    """Основной тест"""
    # Настройка headless-режима для Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Инициализация драйвера Chrome
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    try:
        # Шаг 1: Авторизация
        login(driver, "standard_user", "secret_sauce")

        # Шаг 2: Добавление товара в корзину
        add_item_to_cart(driver, "add-to-cart-sauce-labs-backpack")

        # Шаг 3: Оформление покупки
        checkout(driver, "Alex", "Gek", "123123")

    finally:
        driver.quit()


if __name__ == "__main__":
    run_test()
