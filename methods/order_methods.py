import requests
from data import Urls


class OrderMethods:
    @staticmethod
    def create_order(payload):
        response = requests.post(Urls.ORDER_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    def get_orders():
        response = requests.get(Urls.ORDER_URL)
        return response.json(), response.status_code
