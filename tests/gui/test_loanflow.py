from playwright.sync_api import Page
from src.pages.start_page import StartPage
from src.pages.personal_info import PersonalInfoPage
from tests.test_data import generate_random_loan_applicant


def test_loan_flow_personal_info(page: Page):
    """Testar att man kan välja lånetyp och fylla i personuppgifter"""
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
    page.wait_for_selector("#monthlyIncome")
    page.locator("#monthlyIncome").fill(applicant["income"])
    page.locator("#employmentType").click()
    page.get_by_text("Tillsvidareanställd", exact=True).click()
    page.locator("#employer").fill(applicant["employer"])
    page.get_by_role("button", name="Nästa").click()

    # Lånebelopp
    page.wait_for_selector("#loanAmount")
    page.locator("#loanAmount").fill(applicant["loan_amount"])
    page.get_by_role("button", name="Nästa").click()

    # Sammanställning och skicka in ansökan
    page.get_by_role("button", name="Skicka ansökan").click()

    # Verifiera bekräftelsesidan
    page.get_by_text("Din låneansökan är mottagen och behandlas nu.").wait_for()

    # Klicka på "Tillbaka till startsidan"
    page.get_by_role("button", name="Tillbaka till startsidan").click()
    