import data
from methods.courier_methods import CourierMethods
import allure


class TestLoginCourier:
    @allure.title('Проверка логина курьера')
    def test_login_courier(self):
        payload = data.courier_data
        CourierMethods.create_courier(payload)
        courier_response = CourierMethods.login_courier(payload)
        assert courier_response[0]['id'] and courier_response[1] == 200

    @allure.title('Проверка логина с несуществующими данным')
    def test_login_courier_with_non_existent_data(self):
        payload = data.create_courier_data()
        courier_response = CourierMethods.login_courier(payload)
        assert courier_response[0]['message'] == "Учетная запись не найдена" and courier_response[1] == 404

    @allure.title('Проверка логина курьера без обязательных данных')
    def test_login_courtier_without_any_field(self):
        payload = data.courier_data_without_field()
        courier_response = CourierMethods.login_courier(payload)
        assert (courier_response[0]['message'] == "Недостаточно данных для входа"
                and courier_response[1] == 400)
