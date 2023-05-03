import random

from data.data import Person
from faker import Faker

faker_en = Faker('en_US')
Faker.seed()


def generated_person():
    yield Person(
        password=random.randint(100, 9999),
        email=faker_en.email(),
        first_name=faker_en.first_name(),
        job=faker_en.job(),
    )
