Feature: DemoQA Bookstore Authentication
  As a user
  I want to authenticate with the bookstore application
  So that I can access my account

  Background:
    Given I am on the DemoQA Login page

  Scenario: TC-L1 - Login with valid data
    When I login with valid credentials username "afinapd" password "Afina12345!"
    Then I should be logged in successfully

  Scenario: TC-L2 - Login with invalid data
    When I login with valid credentials username "invalid_user" password "wrong_pass"
    Then I should see an error message