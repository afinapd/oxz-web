from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BookstorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    SEARCH_BOX = (By.ID, "searchBox")
    BOOKS_LIST = (By.CLASS_NAME, "rt-tbody")
    BOOK_ROWS = (By.CLASS_NAME, "rt-tr-group")
    BOOK_IMAGES = (By.CSS_SELECTOR, ".rt-tr-group img")
    BOOK_TITLES = (By.CSS_SELECTOR, ".rt-tr-group .mr-2")
    ROWS_PER_PAGE = (By.CLASS_NAME, "-pageSizeOptions")
    LOGIN_BUTTON = (By.ID, "login")
    USERNAME_LABEL = (By.ID, "userName-value")

    def navigate_to_bookstore(self):
        self.driver.get("https://demoqa.com/books")
        self.wait.until(EC.visibility_of_element_located(self.BOOKS_LIST))

    def search_for_book(self, book_name):
        search = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BOX))
        search.clear()
        search.send_keys(book_name)
        # Wait for search results to update
        self.wait.until(EC.presence_of_element_located(self.BOOKS_LIST))

    def is_book_displayed(self, book_name):
        try:
            # Wait for the table to load
            self.wait.until(EC.presence_of_element_located(self.BOOKS_LIST))
            # Try to find the book by title
            book_link = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, f"//a[contains(text(), '{book_name}')]")
            ))
            return book_link.is_displayed()
        except:
            return False

    def is_books_grid_displayed(self):
        try:
            books = self.wait.until(EC.presence_of_all_elements_located(self.BOOK_ROWS))
            return len(books) > 0
        except:
            return False

    def are_book_images_displayed(self):
        try:
            images = self.wait.until(EC.presence_of_all_elements_located(self.BOOK_IMAGES))
            titles = self.wait.until(EC.presence_of_all_elements_located(self.BOOK_TITLES))
            return len(images) > 0 and len(titles) > 0
        except:
            return False

    def is_pagination_displayed(self):
        try:
            pagination = self.wait.until(EC.visibility_of_element_located(self.ROWS_PER_PAGE))
            return pagination.is_displayed()
        except:
            return False

    def is_login_button_displayed(self):
        try:
            login_button = self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
            return login_button.is_displayed()
        except:
            return False

    def is_username_displayed(self):
        try:
            username = self.wait.until(EC.visibility_of_element_located(self.USERNAME_LABEL))
            return username.is_displayed() and username.text.strip() != ""
        except:
            return False
            
    def is_book_with_id_displayed(self, book_id):
        try:
            # Wait for the table to load
            self.wait.until(EC.presence_of_element_located(self.BOOKS_LIST))
            # Try to find the book by ID
            book_link = self.wait.until(EC.visibility_of_element_located(
                (By.ID, book_id)
            ))
            return book_link.is_displayed()
        except Exception as e:
            print(f"Error finding book with ID {book_id}: {str(e)}")
            return False
            
    def add_book_to_profile(self, book_name):
        try:
            # Click on the book title to open details
            book_link = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//span[@class='mr-2']/a[contains(text(), '{book_name}')]")))
            book_link.click()
            
            # Wait for book details page to load
            self.wait.until(EC.url_contains('book='))
            
            # Click Add to Collection button
            add_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".text-right.fullButton")))
            add_button.click()
            
            # Handle alert
            try:
                alert = self.wait.until(EC.alert_is_present())
                alert_text = alert.text.lower()
                alert.accept()
                return True
            except TimeoutException:
                print("No alert found after clicking add button")
                return False
        except Exception as e:
            print(f"Error adding book: {str(e)}")
            return False
