from selenium.webdriver.common.by import By
import time


def test_find_the_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

