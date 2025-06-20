from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.pages.login_page import LoginPage

@given('I am on the DemoQA Login page')
def step_navigate_to_login(context):
    login_page = LoginPage(context.driver)
    login_page.navigate_to_login()

@when('I login with valid credentials username "{username}" password "{password}"')
def step_login_with_credentials(context, username, password):
    login_page = LoginPage(context.driver)
    login_page.login(username, password)

@then('I should be logged in successfully')
def step_verify_login_success(context):
    # After successful login, we should be redirected to profile page
    WebDriverWait(context.driver, 10).until(
        EC.url_contains('/profile')
    )
    assert 'profile' in context.driver.current_url, "Should be redirected to profile page"

@then('I should see an error message')
def step_verify_error_message(context):
    login_page = LoginPage(context.driver)
    assert login_page.is_error_message_displayed(), "Error message should be displayed"


