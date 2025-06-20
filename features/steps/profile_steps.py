from behave import when, then, given
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.profile_page import ProfilePage
from features.pages.bookstore_page import BookstorePage

@when('I navigate to the Profile page')
def step_navigate_to_profile(context):
    profile_page = ProfilePage(context.driver)
    profile_page.navigate_to_profile()

@then('I should see a message asking me to log in')
def step_verify_login_message(context):
    profile_page = ProfilePage(context.driver)
    assert profile_page.is_login_message_displayed(), \
           "Should see message asking to log in"

@when('I click the "{button}" button')
def step_click_button(context, button):
    profile_page = ProfilePage(context.driver)
    profile_page.click_button(button)

@then('I should be redirected to the login page')
def step_verify_login_redirect(context):
    assert 'login' in context.driver.current_url, \
           "Should be redirected to login page"

@then('I should see the login form')
def step_verify_login_form(context):
    profile_page = ProfilePage(context.driver)
    assert profile_page.is_login_form_displayed(), \
           "Login form should be displayed"

@given('I have one or more books in my profile')
def step_ensure_has_books(context):
    profile_page = ProfilePage(context.driver)
    profile_page.navigate_to_profile()
    
    if not profile_page.has_one_or_more_books():
        # Add a book if none present
        bookstore_page = BookstorePage(context.driver)
        bookstore_page.navigate_to_bookstore()
        bookstore_page.search_for_book("Learning JavaScript Design Patterns")
        assert bookstore_page.add_book_to_profile("Learning JavaScript Design Patterns"), \
               "Failed to add book to profile"

@when('I confirm the deletion in the modal')
def step_confirm_deletion(context):
    profile_page = ProfilePage(context.driver)
    profile_page.confirm_deletion()


