import random

from API.api_library import Library
from data.generator import generated_person


class TestLibrary:
    class TestGetReq(Library):
        """Класс содержит позитивные и негативные проверки методов получения информации о пользователях"""

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

    class TestChangeMethods(Library):
        """Класс содержит позитивные проверки методов добавления, изменения и удаления информации о пользователях """

        def test_post_create(self):
            """Позитивная проверка отправки данных о пользователе сгенерированных случайным образом,
               получения вадидного id в ответе"""

            person = next(generated_person())
            name = person.first_name
            job = person.job
            status_code, body = self.post_create(name, job)
            assert status_code == 201, "Статус кода не соответсвуе ожидаемому"
            assert body["name"] == name
            assert body["job"] == job
            assert int(body["id"]) > 0

        def test_put_update(self):
            """Позитивная проверка изменения методом put данных о пользователе найденного по id"""

            person = next(generated_person())
            name = person.first_name
            job = person.job
            user_id = random.randint(1, 12)
            status_code, body = self.put_update(name, job, str(user_id))
            assert status_code == 200, "Статус кода не соответсвуе ожидаемому"
            assert body["name"] == name, "Имя не изменено"
            assert body["job"] == job, "Данные о работе не изменены"
            assert "updatedAt" in body, "Отсутсвует время изменения"

        def test_patch_update(self):
            """Позитивная проверка изменения методом put данных о пользователе найденного по id"""

            person = next(generated_person())
            name = person.first_name
            job = person.job
            user_id = random.randint(1, 12)
            status_code, body = self.patch_update(name, job, str(user_id))
            assert status_code == 200, "Статус кода не соответсвуе ожидаемому"
            assert body["name"] == name, "Имя не изменено"
            assert body["job"] == job, "Данные о работе не изменены"
            assert "updatedAt" in body, "Отсутсвует время изменения"

        def test_delete(self):
            """Позитивная проверка удаления данных о пользователе найденного по id"""

            user_id = random.randint(1, 12)
            status_code = self.delete_user(str(user_id))
            assert status_code == 204, "Статус кода не соответсвует ожидаемому"

    class TestRegister(Library):
        """Класс содержит позитивные и негативные проверки методов регистрации и авторизации """

        def test_post_register(self):
            """Позитивная проверка возможности регистрации пользователя"""

            email = "eve.holt@reqres.in"
            password = "pistol"
            status_code, body = self.post_register(email, password)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert int(body["id"]) > 0, "id не валиден"
            assert "token" in body, "Токен отсутсвует в ответе"

        def test_post_login(self):
            """Позитивная проверка возможности авторизации пользователя"""

            email = "eve.holt@reqres.in"
            password = "cityslicka"
            status_code, body = self.post_login(email, password)
            assert status_code == 200, "Статус кода не соответсвует ожидаемому"
            assert "token" in body, "Токен отсутсвует в ответе"



