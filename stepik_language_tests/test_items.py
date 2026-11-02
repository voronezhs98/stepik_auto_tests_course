
import time
from selenium.webdriver.common.by import By


def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    time.sleep(30)

    button = browser.find_elements(
        By.CSS_SELECTOR,
        "button.btn-add-to-basket"
    )

    assert len(button) == 1, "Add to basket button not found"
