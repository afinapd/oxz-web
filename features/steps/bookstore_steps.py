from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.bookstore_page import BookstorePage
from features.pages.login_page import LoginPage

@given('I am on the DemoQA Bookstore page')
def step_navigate_to_bookstore(context):
    bookstore_page = BookstorePage(context.driver)
    bookstore_page.navigate_to_bookstore()

@given('I am logged in with username "{username}" and password "{password}"')
def step_login_and_navigate(context, username, password):
    # First login
    login_page = LoginPage(context.driver)
    login_page.navigate_to_login()
    login_page.login(username, password)

@when('I navigate to the Book Store page')
def step_navigate_to_bookstore_page(context):
    bookstore_page = BookstorePage(context.driver)
    bookstore_page.navigate_to_bookstore()

@when('I search for "{book_name}"')
def step_search_for_book(context, book_name):
    bookstore_page = BookstorePage(context.driver)
    bookstore_page.search_for_book(book_name)

@then('I should see the books displayed in a grid')
def step_verify_books_grid(context):
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.is_books_grid_displayed(), \
           "Books should be displayed in a grid"

@then('each book should have an image and a title')
def step_verify_book_images(context):
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.are_book_images_displayed(), \
           "Book should have both image and title"

@then('I should see the rows per page selector')
def step_verify_pagination(context):
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.is_pagination_displayed(), \
           "Rows per page selector should be displayed"

@then('I should see the login button')
def step_verify_login_button(context):
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.is_login_button_displayed(), \
           "Login button should be displayed"

@then('I should see my username displayed')
def step_verify_username_displayed(context):
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.is_username_displayed(), \
           "Username should be displayed"

@then('the book title should be "{title}"')
def step_verify_book_title(context, title):
    book_id = f"see-book-{title}"
    bookstore_page = BookstorePage(context.driver)
    assert bookstore_page.is_book_with_id_displayed(book_id), \
           f"Book with title '{title}' should be displayed"
