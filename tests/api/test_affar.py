from src.helpers.loan_client import LoanApiClient
from tests.test_data import generate_random_loan_applicant


client = LoanApiClient()


def test_create_loan_approved():
    loan_data = generate_random_loan_applicant()
    response = client.create_loan(loan_data)
    body = response.json()
   
    assert response.status_code == 200
    assert body["success"] == True
    assert body["application"]["status"] == "approved"
    assert body["message"] == "Application approved"
    assert body["application"]["first_name"] == loan_data["first_name"]
    assert body["application"]["loan_amount"].isdigit()


def test_create_loan_missing_required_field():
    loan_data = generate_random_loan_applicant()
    del loan_data["email"]
    response = client.create_loan(loan_data)
    assert response.status_code == 400