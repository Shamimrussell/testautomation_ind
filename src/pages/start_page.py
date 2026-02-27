class StartPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://souderbroder-loan-lab.lovable.app/"

    def navigate(self):
        self.page.goto(self.url)

    def select_loan_type(self, loan_type: str):
        self.page.get_by_role("heading", name=loan_type).click()

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()