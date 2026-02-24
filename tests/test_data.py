from faker import Faker
import requests
import random

fake = Faker("sv_SE")

SKATTEVERKET_API_URL = "https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763"

API_EMPLOYMENT_TYPES = [
    "employed",
    "self-employed",
    "unemployed",
    "student",
    "retired",
]

GUI_EMPLOYMENT_TYPES = {
    "employed": "Tillsvidareanställning",
    "self-employed": "Egenföretagare",
    "unemployed": "Arbetssökande",
    "student": "Student",
    "retired": "Pensionär",
}


def get_random_testpersonnummer():
    response = requests.get(SKATTEVERKET_API_URL)
    data = response.json()
    personnummer_lista = [item["testpersonnummer"] for item in data["results"]]
    return random.choice(personnummer_lista)


def generate_random_loan_applicant():
    api_employment = random.choice(list(API_EMPLOYMENT_TYPES))

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "personal_number": get_random_testpersonnummer(),
        "email": fake.email(),
        "loan_amount": str(fake.random_int(min=10000, max=100000, step=5000)),
        "address": fake.street_address(),
        "postcode": fake.postcode(),
        "city": fake.city(),
        "phone": fake.phone_number(),
        "employment_type": api_employment,                        # För API-tester
        "employment_type_gui": GUI_EMPLOYMENT_TYPES[api_employment],  # För GUI-tester
        "employer": fake.company(),
        "income": str(fake.random_int(min=15000, max=100000, step=1000)),
    }