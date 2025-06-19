from methods.order_methods import OrderMethods
import allure


class TestListOrders:
    @allure.title('Проверка списка заказов')
    def test_list_orders(self):
        list_order = OrderMethods.get_orders()
        assert isinstance(list_order[0]['orders'], list) and list_order[1] == 200
