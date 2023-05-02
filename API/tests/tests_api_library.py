import random

from API.api_library import Library


class TestLibrary(Library):

    def test_get_list_users(self):
        number_page = random.randint(1, 100)
        status_code, body = self.get_list_users(number_page)
        assert status_code == 200, "Статус кода не соответсвует"
        assert body["page"] == number_page, "Страница не соответсвует выбранной"

