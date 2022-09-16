import time

from login_page import BasePage, MainPage
from sign_up_page import AccountCreationHelper, AccountRegPage
from faker import Faker

fake = Faker(locale='ru_RU')
email = fake.email()
password = fake.bothify('????-####')


def test_create_account(browser):
    account_creation_page = AccountCreationHelper(browser)
    account_creation_page.go_to_registration_page()

    account_creation_page.fill_field(AccountRegPage.LOCATOR_FIRST_NAME, fake.first_name())
    account_creation_page.fill_field(AccountRegPage.LOCATOR_LAST_NAME, fake.last_name())
    account_creation_page.fill_field(AccountRegPage.LOCATOR_ADDRESS_1, fake.address())
    account_creation_page.fill_field(AccountRegPage.LOCATOR_POSTCODE, fake.numerify('######'))
    account_creation_page.fill_field(AccountRegPage.LOCATOR_CITY, fake.city())
    account_creation_page.fill_field(AccountRegPage.LOCATOR_EMAIL, email)
    account_creation_page.fill_field(AccountRegPage.LOCATOR_PHONE, fake.numerify('+7#########'))
    account_creation_page.fill_field(AccountRegPage.LOCATOR_DESIRED_PASSWORD, password)
    account_creation_page.fill_field(AccountRegPage.LOCATOR_CONFIRM_PASSWORD, password)
    time.sleep(3)

    account_creation_page.click_on_create_account_button()
    time.sleep(3)

    notification_text = account_creation_page.get_notification_text()
    assert "customer account has been created" in notification_text


def test_log_out(browser):
    base_page = BasePage(browser)
    logout_button = base_page.find_element(MainPage.LOCATOR_LOGOUT_BUTTON)
    logout_button.click()
    time.sleep(7)

    notification_elem = base_page.driver.find_element_by_xpath(MainPage.LOCATOR_NOTIFICATION_AREA)
    notification_elem_text = notification_elem.text
    assert "now logged out" in notification_elem_text
