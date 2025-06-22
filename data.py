from faker import Faker


class Urls:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'
    ORDER_URL = f"{BASE_URL}/orders"
    COURIER_URL = f"{BASE_URL}/courier"
    LOGIN_URL = f"{BASE_URL}/courier/login"


fake = Faker()

LOGIN = fake.last_name()
PASSWORD = fake.random_int()
FIRST_NAME = fake.first_name()
LAST_NAME = fake.last_name()


def create_courier_data():
    payload = {
        "login": f"{fake.last_name()}{fake.uuid4()}",
        "password": f"{fake.random_int()}",
        "firstName": f"{fake.first_name()}"
    }
    return payload


courier_data = create_courier_data()


def courier_data_without_field():
    payload = {
        "login": "",
        "password": f"{PASSWORD}",
        "firstName": f"{FIRST_NAME}"
    }
    return payload


order_info = [
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["GRAY"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK", "GRAY"]
    },
    {
        "firstName": f"{fake.first_name()}",
        "lastName": f"{fake.last_name()}",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
    }
]
