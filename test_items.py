from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_languages(browser):
    browser.get(link)
    basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket
