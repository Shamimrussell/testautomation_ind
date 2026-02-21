import pytest
from config import API_KEY, BASE_URL, ADMIN_API_KEY
from helpers.loan_client import LoanClient

@pytest.fixture(scope="session")
def api_client():
    return LoanClient(
       base_url = BASE_URL, 
       api_key = API_KEY,
       admin_api_key = ADMIN_API_KEY,
       )