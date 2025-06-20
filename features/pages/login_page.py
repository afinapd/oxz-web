from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login")
    NEW_USER_BUTTON = (By.ID, "newUser")
    ERROR_MESSAGE = (By.ID, "name")

    def navigate_to_login(self):
        self.driver.get("https://demoqa.com/login")
        try:
            # First try to find the username input directly
            self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        except TimeoutException:
            # If not found, try to click the login button from the header if present
            try:
                header_login = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
                header_login.click()
                # Now wait for the username input
                self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
            except TimeoutException:
                raise TimeoutException("Could not find login form elements")

    def login(self, username, password):
        try:
            # Clear and fill username field
            username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
            username_field.clear()
            username_field.send_keys(username)
            
            # Clear and fill password field
            password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
            password_field.clear()
            password_field.send_keys(password)
            
            # Click login button using JavaScript to bypass any ads
            login_button = self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))
            self.driver.execute_script("arguments[0].click();", login_button)
            
            # Handle any alerts that might appear
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text
                alert.accept()
                raise Exception(f"Login failed: {alert_text}")
            except TimeoutException:
                pass  # No alert appeared, which is good
            
            # Wait for redirect to profile or error message
            self.wait.until(lambda driver: 
                'profile' in driver.current_url or 
                self.is_error_message_displayed())
                
        except Exception as e:
            raise Exception(f"Login failed: {str(e)}")

    def click_new_user(self):
        new_user_button = self.wait.until(EC.element_to_be_clickable(self.NEW_USER_BUTTON))
        self.driver.execute_script("arguments[0].click();", new_user_button)

    def is_error_message_displayed(self):
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return error_element.is_displayed()
        except:
            return False

    def get_error_message(self):
        if self.is_error_message_displayed():
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        return None
