from WEB.pages.base_page import BasePage
from WEB.locators.main_page_locators import MainPageLocators


class Requests(BasePage):
    locators = MainPageLocators()

    def click_get_list_users(self):
        button = self.element_is_visible(self.locators.GET_LIST_USERS)
        self.go_to_element(button)
        button.click()
        status_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        return status_code
