import allure
import requests
from data import Urls


class CourierMethods:

    @staticmethod
    @allure.step('Создаём курьера')
    def create_courier(payload):
        response = requests.post(Urls.COURIER_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Логинимся')
    def login_courier(payload):
        response = requests.post(Urls.LOGIN_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(courier_id):
        requests.delete(f"{Urls.COURIER_URL}/{courier_id}")
