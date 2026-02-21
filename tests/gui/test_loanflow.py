import pytest
from playwright.sync_api import Page
from src.pages.start_page import StartPage
from src.pages.personal_info import PersonalInfoPage
from tests.test_data import generate_loan_applicant

def test_loan_flow_personal_info(page: Page):
