link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_cart_button_presented(browser):
    browser.get(link)
    cartButton = browser.find_elements_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    #check if only one button is found
    assert len(cartButton) == 1, "Cart button is not presented in the page"