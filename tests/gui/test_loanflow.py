from playwright.sync_api import Page
from src.pages.start_page import StartPage
from src.pages.personal_info import PersonalInfoPage
from src.pages.income_page import IncomePage
from src.pages.loan_amount import LoanAmountPage
from tests.test_data import generate_random_loan_applicant


def test_loan_flow_personal_info(page: Page):
    #Testar att man kan välja lånetyp och fylla i personuppgifter
    applicant = generate_random_loan_applicant()

    # Startsidan
    start = StartPage(page)
    start.navigate()
    start.select_loan_type("Bil")
    start.click_next()

    # Personuppgifter
    personal = PersonalInfoPage(page)
    personal.fill_all(applicant)
    personal.click_next()

    # Kontrollera att vi kom vidare till steg 2
    assert page.get_by_role("heading", name="Inkomstuppgifter").is_visible()

    # Inkomst
    income_page = IncomePage(page)
    income_page.fill_income_information(applicant, applicant["employment_type_gui"])

    # Lånebelopp
    page.wait_for_selector("#loanAmount")
    loan_amount_page = LoanAmountPage(page)
    loan_amount_page.fill_all(applicant)

    # Sammanställning och skicka in ansökan
    page.get_by_role("button", name="Skicka ansökan").click()

    # Verifiera bekräftelsesidan
    page.get_by_text("Din låneansökan är mottagen och behandlas nu.").wait_for()

    # Klicka på "Tillbaka till startsidan"
    page.get_by_role("button", name="Tillbaka till startsidan").click()
    