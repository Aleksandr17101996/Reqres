from selenium.webdriver.common.by import By


class MainPageLocators:
    """Класс содержит локаторы кнопок отправки образца запросов на главной странице сайта"""

    GET_LIST_USERS = (By.CSS_SELECTOR, 'li[data-id="users"]')
    GET_SINGLE_USER = (By.CSS_SELECTOR, 'li[data-id="users-single"]')
    GET_SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="users-single-not-found"]')
    GET_LIST_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown"]')
    GET_SINGLE_RES_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"]')
    POST_CREATE = (By.CSS_SELECTOR, 'li[data-id="post"]')
    PUT_UPDATE = (By.CSS_SELECTOR, 'li[data-id="put"]')
    PATCH_UPDATE = (By.CSS_SELECTOR, 'li[data-id="patch"]')
    DELETE = (By.CSS_SELECTOR, 'li[data-id="delete"]')
    POST_REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-successful"]')
    POST_REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"]')
    POST_LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-successful"]')
    POST_LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-unsuccessful"]')
    GET_DELAYED_RESPONSE = (By.CSS_SELECTOR, 'li[data-id="delay"]')
    RESPONSE_CODE = (By.CSS_SELECTOR, 'span[class="response-code"]')
    BODY_RESPONSE = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')
    OUTPUT_REQUEST = (By.CSS_SELECTOR, 'pre[data-key="output-request"]')
