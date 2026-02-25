import sys
import os
import pytest
from src.helpers.loan_client import LoanApiClient
sys.path.insert(0, os.path.dirname(__file__))


@pytest.fixture
def client():
    return LoanApiClient()