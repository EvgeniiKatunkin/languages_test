import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_if_button_exists(browser):
    browser.get(link)
    # time.sleep(10)

    try:
        button = browser.find_element(By.CLASS_NAME, "btn-primary")
        flag = True
    except NoSuchElementException:
        flag = False

    assert flag, f"There is no button on the page {link}"
