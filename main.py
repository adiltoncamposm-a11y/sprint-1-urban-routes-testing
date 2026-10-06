from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver = webdriver.Chrome()

    driver.get("https://www.saucedemo.com")

    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    add_to_cart = driver.find_element(
        By.ID,
        "add-to-cart-sauce-labs-backpack"
    )
    add_to_cart.click()

    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")

    add_to_cart_2 = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
    add_to_cart_2.click()
    assert cart_badge.text == "2"
    driver.quit()