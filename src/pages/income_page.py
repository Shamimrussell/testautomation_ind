class IncomePage:

    def __init__(self, page):
        self.page = page

    def fill_income_information(self, applicant, employment_gui_value):
        self.page.locator("#monthlyIncome").fill(applicant["income"])
        self.page.locator("#employmentType").click()
        self.page.get_by_text(employment_gui_value, exact=True).click()
        self.page.locator("#employer").fill(applicant["employer"])
        self.page.get_by_role("button", name="Nästa").click()