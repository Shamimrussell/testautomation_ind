import pytest
from src.helpers.loan_client import LoanApiClient
from tests.test_data import generate_random_loan_applicant


def test_create_loan_approved(client):
    loan_data = generate_random_loan_applicant()
    response = client.create_loan(loan_data)
    body = response.json()
   
    assert response.status_code == 200
    assert body["success"] == True
    assert body["application"]["status"] == "approved"
    assert body["message"].startswith("Application approved")
    assert body["application"]["first_name"] == loan_data["first_name"]
    assert body["application"]["loan_amount"].isdigit()


@pytest.mark.parametrize("loan_amount, expected_status_code", [
    ("50000", 200),   # Normalt belopp → godkänt
    ("99000", 200),   # Precis under gränsen → godkänt
    ("100001", 400),  # Över partnergränsen → fel
    ("150000", 400),  # Långt över → fel
])


def test_loan_amount_limits(client, loan_amount, expected_status_code):
    """Testar gränsvärden för max lånebelopp"""
    loan_data = generate_random_loan_applicant()
    loan_data["loan_amount"] = loan_amount
    
    response = client.create_loan(loan_data)
    assert response.status_code == expected_status_code


def test_create_loan_missing_required_field(client):
    loan_data = generate_random_loan_applicant()
    del loan_data["email"]
    response = client.create_loan(loan_data)
    assert response.status_code == 400