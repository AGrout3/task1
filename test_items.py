from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    testable_object = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")))
    assert testable_object, "Тестируемый обьект отсутствует на странице"
    time.sleep(0)

    #