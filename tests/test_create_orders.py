import pytest
import json
import allure

import data
from methods.order_methods import OrderMethods


class TestOrders:
    @allure.title('Проверка создания заказа')
    @pytest.mark.parametrize("order_data", data.order_info)
    def test_create_order(self, order_data):
        order_json = json.dumps(order_data)
        order_response = OrderMethods.create_order(order_json)
        assert order_response[0]['track'] and order_response[1] == 201

