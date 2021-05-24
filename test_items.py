from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_assert_button_diff_language(browser):
    browser.get(link)
    time.sleep(5)
    # Проверяем, что элемент присутствует на странице
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form")))
