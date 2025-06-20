Feature: DemoQA Profile
  As a user
  I want to manage my profile and books
  So that I can organize my collection


  @test
  Scenario: TC-P1 - Access profile without login
    When I navigate to the Profile page
    Then I should see a message asking me to log in

  Scenario: TC-P2 - Logout from profile
    Given I am logged in with username "afinapd" and password "Afina12345!"
    When I navigate to the Profile page
    And I click the "Log out" button
    Then I should be redirected to the login page
    And I should see the login form

  Scenario: TC-P3 - Delete books from profile
    Given I am logged in with username "afinapd" and password "Afina12345!"
    When I navigate to the Profile page
    And I click the "Delete All Books" button
    And I confirm the deletion in the modal
