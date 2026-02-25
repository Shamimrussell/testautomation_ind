class LoanAmountPage:
    def __init__(self, page):
        self.page = page

    def fill_loan_amount(self, amount: str):
        self.page.wait_for_selector("#loanAmount")
        self.page.locator("#loanAmount").fill(amount)

    def click_calculate(self):
        self.page.get_by_role("button", name="Beräkna månadskostnad").click()

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()

    def fill_all(self, data: dict):
        self.fill_loan_amount(data["loan_amount"])
        self.click_next()