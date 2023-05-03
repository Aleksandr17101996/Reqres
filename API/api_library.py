import requests
from API.config import Base


class Library:
    url = Base.BASE_URL
    v1 = Base.API_V1

    """Библиотека api"""

    def get_list_users(self, page_number):
        """Метод делает запрос к API сервера и возвращает статус кода и результат в формате
           JSON с списком пользователей, найденных на выбранной странице"""

        params = {'page': page_number}
        r = requests.get(self.url + self.v1 + "users", params=params)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_single_user(self, user_id):
        """Метод делает запрос к API сервера и возвращает статус кода и результат в формате
           JSON с данными о пользователе найденному по ID"""

        r = requests.get(self.url + self.v1 + "users/" + str(user_id))
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_list_resource(self):
        """Метод делает запрос к API сервера и возвращает статус кода и результат в формате
           JSON с данными о пользователях"""

        r = requests.get(self.url + self.v1 + "unknown")
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_single_resource(self, user_id):
        """Метод делает запрос к API сервера и возвращает статус кода и результат в формате
           JSON с данными о пользователе найденному по ID"""

        r = requests.get(self.url + self.v1 + "unknown/" + user_id)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def post_create(self, name, job):
        """Метод отправляет на сервер данные о имене и работе пользователея возвращает присвоенный
        id и дату операции"""

        data = {
            "name": name,
            "job": job
        }
        r = requests.post(self.url + self.v1 + "users", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def put_update(self, name, job, user_id):
        """Тест"""

        data = {
            "name": name,
            "job": job
        }
        r = requests.put(self.url + self.v1 + "users/" + user_id, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def patch_update(self, name, job, user_id):
        """Тест"""

        data = {
            "name": name,
            "job": job
        }
        r = requests.patch(self.url + self.v1 + "users/" + user_id, json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def delete_user(self, user_id):
        """Тест"""

        r = requests.delete(self.url + self.v1 + "users/" + user_id)
        status_code = r.status_code
        return status_code

    def post_register(self, email, password):
        """Тест"""

        data = {
            "email": email,
            "password": password
        }
        r = requests.post(self.url + self.v1 + "register", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def post_login(self, email, password):
        """Тест"""

        data = {
            "email": email,
            "password": password
        }
        r = requests.post(self.url + self.v1 + "login", json=data)
        status_code = r.status_code
        body = r.json()
        return status_code, body

    def get_delayed_response(self, seconds):
        """Тест"""

        params = {"delay": seconds}
        r = requests.get(self.url + self.v1 + "users", params=params)
        status_code = r.status_code
        body = r.json()
        return status_code, body
