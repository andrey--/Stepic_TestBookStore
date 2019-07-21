import time
from selenium.common.exceptions import NoSuchElementException


class TestBookStore:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    def test_guest_should_see_add_to_basket_button(self, browser):
        browser.get(self.link)
        time.sleep(30)
        try:
            browser.find_element_by_css_selector("button.btn-add-to-basket")
            button_found = True
        except NoSuchElementException:
            button_found = False
        assert button_found
