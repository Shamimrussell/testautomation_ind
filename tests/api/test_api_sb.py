import requests
from config import API_KEY, BASE_URL
import pytest
from helpers.loan_client import LoanClient

@pytest.fixture
def api():
    return LoanClient(BASE_URL, API_KEY, None)

#"tekniskt" test mha requests-biblioteket, där headers, HTTP statuskod mm valideras
def test_():

    




#"affärs"-test mha requests-biblioteket, där del av JSON-svaret/body:n valideras