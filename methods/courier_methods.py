import requests
from data import Urls


class CourierMethods:

    @staticmethod
    def create_courier(payload):
        response = requests.post(Urls.COURIER_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    def login_courier(payload):
        response = requests.post(Urls.LOGIN_URL, data=payload)
        return response.json(), response.status_code
