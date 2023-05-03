import time

from WEB.pages.main_page import Requests


class TestRequests:
    class TestMain:

        def test_click_get_list_users(self, driver):
            requests_page = Requests(driver, 'https://reqres.in/')
            requests_page.open()
            status = requests_page.click_get_list_users()
            print(status)
            time.sleep(10)
