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

        def test_click_get_single_user(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователе,
               возвращается статус кода 200, в теле ответа есть информация о пользователе """

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_single_user()
            status_code = page.check_status_code()
            body = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert "data" in body

        def test_click_get_single_user_not_fo(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователе,
               через несуществующий id, возвращается статус кода 404"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_single_user_not_found()
            status_code = page.check_status_code_bud()
            assert status_code == 404, "Статус кода несоответсвует ожидаемому"

        def test_click_get_list_resource(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователях,
               возвращается статус кода 200 и отображается информация о 6 пользователях """

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_list_resource()
            status_code = page.check_status_code()
            body = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует"
            assert len(body['data']) == 6, "Не верное колличество пользователей на странице"

        def test_click_get_single_resource(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователе,
               возвращается статус кода 200, в теле ответа есть информация о пользователе """

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_single_resource()
            status_code = page.check_status_code()
            body = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert body['data']['name'] == "fuchsia rose", "Име в теле ответа не соответсвувеет"
