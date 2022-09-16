from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    LOCATOR_EMAIL = "//input[@name='email']"
    LOCATOR_PASSWORD = "//input[@name='password']"
    LOCATOR_LOGIN_BUTTON = "//button[@name='login']"
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, "//div[@id='box-account']//a[contains(@href,'logout')]")
    LOCATOR_NOTIFICATION_AREA = "//div[@class='notice success']"


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://litecart.stqa.ru/ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_registration_page(self):
        return self.driver.get(self.base_url + 'create_account')
