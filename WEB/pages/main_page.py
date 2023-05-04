import json
import time

from WEB.pages.base_page import BasePage
from WEB.locators.main_page_locators import MainPageLocators


class Requests(BasePage):
    locators = MainPageLocators()

    def click_get_list_users(self):
        """Метод кликает на кнопку Get list users"""

        button = self.element_is_visible(self.locators.GET_LIST_USERS)
        self.go_to_element(button)
        button.click()

    def check_status_code(self):
        """Метод находит и возвращает статус код указанный на главной странице"""

        status_code = self.element_is_present(self.locators.RESPONSE_CODE).text
        return int(status_code)

    def check_status_code_bud(self):
        """Метод находит и возвращает статус код указанный на главной странице"""

        status_code = self.element_is_present(self.locators.RESPONSE_CODE_BUD).text
        return int(status_code)

    def check_result(self):
        """Метод находит и возвращает тело ответа взятое с главной страницы сайта"""

        body = self.element_is_visible(self.locators.BODY_RESPONSE).text
        return json.loads(body)

    def click_get_single_user(self):
        """Метод кликает на кнопку Get single user"""

        button = self.element_is_visible(self.locators.GET_SINGLE_USER)
        self.go_to_element(button)
        button.click()

    def click_get_single_user_not_found(self):
        """Метод кликает на кнопку Get single user not found"""

        button = self.element_is_visible(self.locators.GET_SINGLE_USER_NOT_FOUND)
        self.go_to_element(button)
        button.click()

    def click_get_list_resource(self):
        """Метод кликает на кнопку Get list resource"""
        button = self.element_is_visible(self.locators.GET_LIST_RESOURCE)
        self.go_to_element(button)
        button.click()

    def click_get_single_resource(self):
        """Метод кликает на кнопку Get single resource"""

        button = self.element_is_visible(self.locators.GET_SINGLE_RESOURCE)
        self.go_to_element(button)
        button.click()


