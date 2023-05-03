import random

from API.api_library import Library


class TestLibrary:
    class TestGetReq(Library):
        """Класс содержит позитивные и негативные проверки get методов """
        def test_get_list_users(self):
            """Позитивная проверка предоставления информации о пользователях
               на случайно выбранной странице"""

            number_page = random.randint(1, 100)
            status_code, body = self.get_list_users(number_page)
            assert status_code == 200, "Статус кода не соответсвует"
            assert body["page"] == number_page, "Страница не соответсвует выбранной"

        def test_single_user(self):
            """Позитивная проверка предоставления информации о случайном пользователе
               выбранным случайным образом по id"""

            user_id = random.randint(1, 12)
            status_code, body = self.get_single_user(user_id)
            assert status_code == 200, "Статус кода не соответсвует"
            assert body["data"]["id"] == user_id, "Найден пользователь с несоответсвующем id"

        def test_list_resource(self):
            """Позитивная проверка предоставления информации о пользователях"""

            status_code, body = self.get_list_resource()
            assert status_code == 200, "Статус кода не соответсвуе ожидаемому"
            assert body['data'][0]['id'] == 1, "id первого пользователя не соответсвует"

        def test_single_resource(self):
            """Позитивная проверка предоставления информации о случайном пользователе
               выбранным случайным образом по id"""

            user_id = random.randint(1, 12)
            status_code, body = self.get_single_resource(str(user_id))
            assert status_code == 200, "Статус кода не соответсвуе ожидаемому"
            assert body["data"]["id"] == user_id, "Найден пользователь с несоответсвующем id"

        def test_get_list_users_neg(self):
            """Негативная проверка предоставления информации о пользователе
               выбранным случайным образом по несуществующему id"""

            user_id = random.randint(13, 100)
            status_code, body = self.get_single_user(user_id)
            assert status_code == 404, "Статус кода не соответсвует"
            assert body == {}, "Тело ответа не пустое"

        def test_single_resource_neg(self):
            """Негативная проверка предоставления информации о случайном пользователе
               выбранным случайным образом по несущестующему id"""

            user_id = random.randint(13, 100)
            status_code, body = self.get_single_resource(str(user_id))
            assert status_code == 404, "Статус кода не соответсвуе ожидаемому"
            assert body == {}, "Тело ответа не пустое"