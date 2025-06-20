from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    LOGIN_MESSAGE = (By.CLASS_NAME, "rt-noData")
    LOGIN_FORM = (By.ID, "userForm")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log out']")
    DELETE_ALL_BOOKS_BUTTON = (By.XPATH, "//button[text()='Delete All Books']")
    MODAL_OK_BUTTON = (By.ID, "closeSmallModal-ok")
    BOOKS_LIST = (By.CLASS_NAME, "rt-tbody")
    BOOK_ROWS = (By.CLASS_NAME, "rt-tr-group")


    def navigate_to_profile(self):
        self.driver.get("https://demoqa.com/profile")

    def is_login_message_displayed(self):
        try:
            # Look for the text with login and register links
            login_link = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[text()='login']")
            ))
            register_link = self.wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[text()='register']")
            ))
            return login_link.is_displayed() and register_link.is_displayed()
        except Exception as e:
            print(f"Error finding login message: {str(e)}")
            return False

    def is_login_form_displayed(self):
        try:
            form = self.wait.until(EC.visibility_of_element_located(self.LOGIN_FORM))
            return form.is_displayed()
        except:
            return False

    def click_button(self, button_text):
        try:
            button_locator = (By.XPATH, f"//button[text()='{button_text}']")
            button = self.wait.until(EC.element_to_be_clickable(button_locator))
            button.click()
        except Exception as e:
            print(f"Error clicking {button_text} button: {str(e)}")

    def confirm_deletion(self):
        try:
            # Wait for modal to be visible
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-content")))
            
            # Click OK button
            ok_button = self.wait.until(EC.element_to_be_clickable(self.MODAL_OK_BUTTON))
            ok_button.click()
            
            # Wait for alert and accept it
            alert = self.wait.until(EC.alert_is_present())
            alert.accept()
        except Exception as e:
            print(f"Error confirming deletion: {str(e)}")

    def has_one_or_more_books(self):
        try:
            books = self.wait.until(EC.presence_of_all_elements_located(self.BOOK_ROWS))
            return any(book.text.strip() for book in books)
        except:
            return False


