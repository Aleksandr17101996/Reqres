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

        def test_click_get_sin_res_not_fou(self, driver):
            """Проверяем что при нажатии на отправку запроса о полчении информации о пользователе,
               через несуществующий id, возвращается статус кода 404"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_single_res_not_fo()
            status_code = page.check_status_code_bud()
            assert status_code == 404, "Статус кода несоответсвует ожидаемому"

        def test_post_create(self, driver):
            """Проверяем что при нажатии на отправку post запроса с данными о пользователе,
                возвращается статус кода 201, передаваемые данные в запросе присутсвуют в ответе
                присвоен валидный id, так же указанно время и дата операции"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_post_create()
            request = page.check_out_req()
            status_code = page.check_status_code()
            response = page.check_result()
            assert status_code == 201, "Статус кода не соответсвует"
            assert request["name"] == response["name"], "Передоваемое имя в запросе отстутсвует в ответе"
            assert request["job"] == response["job"], "Сведенья о работе  в ответе не соответсвуют"
            assert int(response['id']) > 0, "id невалидный"
            assert 'createdAt' in response, "Отсутсвует дата выполнения операции"

        def test_put_update(self, driver):
            """Проверяем что при нажатии на отправку put запроса на обнавление данных о пользователе,
               возвращается статус кода 200, передаваемые данные в запросе присутсвуют в ответе
               так же указанно время и дата операции"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_put_update()
            request = page.check_out_req()
            status_code = page.check_status_code()
            response = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует"
            assert request["name"] == response["name"], "Передоваемое имя в запросе отстутсвует в ответе"
            assert request["job"] == response["job"], "Сведенья о работе  в ответе не соответсвуют"
            assert "updatedAt" in response, "Нет данных о дате и времени изменения"

        def test_patch_update(self, driver):
            """Проверяем что при нажатии на отправку path запроса на обнавление данных о пользователе,
               возвращается статус кода 200, передаваемые данные в запросе присутсвуют в ответе
               так же указанно время и дата операции"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_patch_update()
            request = page.check_out_req()
            status_code = page.check_status_code()
            response = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует"
            assert request["name"] == response["name"], "Передоваемое имя в запросе отстутсвует в ответе"
            assert request["job"] == response["job"], "Сведенья о работе  в ответе не соответсвуют"
            assert "updatedAt" in response, "Нет данных о дате и времени изменения"

        def test_delete(self, driver):
            """Проверяем что при нажатии на отправку delete запроса на удаление данных о пользователе,
               возвращается статус кода 204"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_delete()
            status_code = page.check_status_code_bud()
            assert status_code == 204, "Статус кода не соответсвует ожидаемому"

        def test_post_register_successful(self, driver):
            """Проверяем что при нажатии на отправку post запроса на регистрацию пользователе,
               возвращается статус кода 200, присвоен валидный id и в ответе содержится токен"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_post_register_successful()
            status_code = page.check_status_code()
            response = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует"
            assert int(response["id"]) > 0, "id не валиден"
            assert "token" in response, "Токен отсутсвует в ответе"

        def test_post_register_unsuccessful(self, driver):
            """Проверяем что при нажатии на отправку post запроса на регистрацию пользователе,без передачи пароля
               возвращается статус кода 400, в ответе содержится описание ошибки"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_post_register_unsuccessful()
            status_code = page.check_status_code_bud()
            response = page.check_result()
            assert status_code == 400, "Статус кода не соответсвует"
            assert response["error"] == "Missing password", "Ошибка не обрабатывается системой"

        def test_post_login_successful(self, driver):
            """Проверяем что при нажатии на отправку post запроса на авторизацию пользователе,
               возвращается статус кода 200, в ответе содержится токен"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_login_successful()
            status_code = page.check_status_code()
            response = page.check_result()
            assert status_code == 200, "Статус кода не соответсвует"
            assert "token" in response

        def test_post_login_unsuccessful(self, driver):
            """Проверяем что при нажатии на отправку post запроса на авторизацию пользователе,без передачи пароля
               возвращается статус кода 400, в теле ответа возвращается описание ошибки"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_login_unsuccessful()
            status_code = page.check_status_code_bud()
            response = page.check_result()
            assert status_code == 400, "Статус кода не соответсвует"
            assert response["error"] == "Missing password", "Ошибка не обрабатывается системой"

        def test_get_delayed_response(self, driver):
            """Проверяем что при нажатии на отправку post запроса на авторизацию пользователе,без передачи пароля
               возвращается статус кода 400, в теле ответа возвращается описание ошибки"""

            page = Requests(driver, 'https://reqres.in/')
            page.open()
            page.click_get_delayed_response()
            response = page.check_result()
            status_code = page.check_status_code()
            assert status_code == 200, "Стаатус кода не соответсвует ожидаемому"
            assert len(response["data"]) == 6, "Колличеество пользователей на странице не соотвентсвует"