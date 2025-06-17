import random

from faker import Faker

import data

faker = Faker('ru_RU')


def generate_order_field():
    name = faker.first_name()
    middle_name = faker.last_name()
    address = (faker.address().replace('\n', ' ').replace(',', '').replace('.', '')
               .replace(')', '').replace('(', '').replace('!', '').replace('/', '')
               .strip())[:49]
    metro = random.randint(0, 224)
    number = f"8{random.randint(9000000000, 9999999999)}"
    return name, middle_name, address, metro, number


def generate_rental_field():
    when_data = faker.future_datetime()
    when = when_data.strftime("%d.%m.%Y")
    period_id = random.choice(data.Data.period)
    colour = random.choice(data.Data.colours)
    comment = faker.text()
    return when, period_id, colour, comment
