class PersonalInfoPage:
    def __init__(self, page):
        self.page = page

    def fill_personal_number(self, personal_number):
        self.page.wait_for_selector("#personalNumber")
        # Tar bort de första 2 siffrorna (seklet) om det är 12 siffror
        pnr = personal_number[-10:] if len(personal_number) == 12 else personal_number
        self.page.locator("#personalNumber").fill(pnr)

    def fill_first_name(self, first_name):
        self.page.locator("#firstName").fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator("#lastName").fill(last_name)

    def fill_email(self, email):
        self.page.locator("#email").fill(email)

    def fill_phone(self, phone):
        self.page.locator("#phone").fill(phone)

    def fill_address(self, address):
        self.page.locator("#address").fill(address)

    def fill_postal_code(self, postal_code):
        self.page.locator("#postalCode").fill(postal_code)

    def fill_city(self, city):
        self.page.locator("#city").fill(city)

    def click_next(self):
        self.page.get_by_role("button", name="Nästa").click()

    def fill_all(self, data: dict):
        """Fyller i hela formuläret med en dict"""
        self.fill_personal_number(data["personal_number"])
        self.fill_first_name(data["first_name"])
        self.fill_last_name(data["last_name"])
        self.fill_email(data["email"])
        self.fill_phone(data["phone"])
        self.fill_address(data["address"])
        self.fill_postal_code(data["postcode"])
        self.fill_city(data["city"])