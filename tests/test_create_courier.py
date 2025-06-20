import allure
import pytest

import data
from methods.courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('Проверка создания курьера')
    def test_create_courier(self, courier_create):
        courier_response = courier_create
        assert courier_response[0]['ok'] and courier_response[1] == 201

    @allure.title('Проверка невозможности создания курьеров с одинаковыми данными')
    def test_recreation_courier(self, courier_create):
        payload = data.courier_data
        courier_response = CourierMethods.create_courier(payload)
        assert (courier_response[0]['message'] == "Этот логин уже используется. Попробуйте другой."
                and courier_response[1] == 409)

    @allure.title('Проверка невозможности создания курьеров без обязательных полей')
    def test_create_courtier_without_any_field(self):
        payload = data.courier_data_without_field()
        courier_response = CourierMethods.create_courier(payload)
        assert (courier_response[0]['message'] == "Недостаточно данных для создания учетной записи"
                and courier_response[1] == 400)

