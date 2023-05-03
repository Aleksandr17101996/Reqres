import time

from WEB.pages.main_page import Requests


class TestRequests:
    class TestMain:

        def test_click_get_list_users(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователях на 2 странице,
               возвращается статус кода 200 и отображается информация о 6 пользователях """

            requests_page = Requests(driver, 'https://reqres.in/')
            requests_page.open()
            requests_page.click_get_list_users()
            status_code = requests_page.check_status_code()
            body = requests_page.check_result()
            assert len(body['data']) == 6, "Не верное колличество пользователей на странице"
            assert status_code == 200, "Статус кода не соответсвует"
