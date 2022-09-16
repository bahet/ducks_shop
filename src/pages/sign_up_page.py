from selenium.webdriver.common.by import By
from login_page import BasePage


class AccountRegPage:
    LOCATOR_FIRST_NAME = (By.NAME, "firstname")
    LOCATOR_LAST_NAME = (By.NAME, "lastname")
    LOCATOR_ADDRESS_1 = (By.NAME, "address1")
    LOCATOR_POSTCODE = (By.NAME, "postcode")
    LOCATOR_CITY = (By.NAME, "city")
    LOCATOR_COUNTRY = (By.NAME, "country_code")
    LOCATOR_EMAIL = (By.NAME, "email")
    LOCATOR_PHONE = (By.NAME, "phone")
    LOCATOR_DESIRED_PASSWORD = (By.NAME, "password")
    LOCATOR_CONFIRM_PASSWORD = (By.NAME, "confirmed_password")
    LOCATOR_CREATE_ACCOUNT_BUTTON = (By.NAME, "create_account")
    LOCATOR_ACCOUNT_CREATION_NOTIFICATION = "//div[@class='notice success']"


class AccountCreationHelper(BasePage):

    def fill_field(self, locator, value):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(value)
        return search_field

    def click_on_create_account_button(self):
        return self.find_element(AccountRegPage.LOCATOR_CREATE_ACCOUNT_BUTTON, time=2).click()

    def get_notification_text(self):
        text = self.driver.find_element_by_xpath(AccountRegPage.LOCATOR_ACCOUNT_CREATION_NOTIFICATION).text
        return text
