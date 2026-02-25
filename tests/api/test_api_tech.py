from src.helpers.loan_client import LoanApiClient
import requests
from config import BASE_URL


#"tekniskt" test mha requests-biblioteket, där headers, HTTP statuskod mm valideras
def test_get_status(client):
    response = client.get_loans()
    assert response.status_code == 200
    assert "application/json" in response.headers["Content-Type"]

def test_get_without_key(client):
    response = requests.get(f"{BASE_URL}/partner-loan-api")
    assert response.status_code ==401

