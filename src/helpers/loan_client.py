import requests
from config import API_KEY, BASE_URL, ADMIN_API_KEY


class LoanApiClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "x-api-key": API_KEY,
            "x-admin-api-key": ADMIN_API_KEY
        }


    def get_loans(self):
        return requests.get(
            f"{self.base_url}/partner-loan-api",
            headers=self.headers
        )


    def create_loan(self, loandata):
        return requests.post(
            f"{self.base_url}/partner-loan-api",
            json=loandata,
            headers=self.headers
        )


    def update_loan(self, payload):
        return requests.put(
            f"{self.base_url}/partner-loan-api",
            json=payload,
            headers=self.headers)
    

    def delete_loan(self, reference_number):
        return requests.delete(
            f"{self.base_url}/partner-loan-api",
            params={"reference_number": reference_number},
            headers=self.headers
        )