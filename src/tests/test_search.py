from selenium.webdriver.common.by import By


class TestSearch:

    def test_find_input_success(self, search_page):
        selector = "#search_form_input_homepage"
        search_input = search_page.find_element(By.CSS_SELECTOR, selector)
        assert search_input

    def test_find_input_error(self, search_page):
        selector = "#search"
        search_input = search_page.find_element(By.CSS_SELECTOR, selector)
        assert search_input
