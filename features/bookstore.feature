Feature: DemoQA Bookstore
  As a user
  I want to interact with the bookstore application
  So that I can view and search for books

  Background:
    Given I am on the DemoQA Bookstore page

  Scenario: TC-B1 - View list of books (public)
    Then I should see the books displayed in a grid
    And each book should have an image and a title
    And I should see the rows per page selector
    And I should see the login button

  Scenario: TC-B2 - View list of books (after login)
    Given I am logged in with username "afinapd" and password "Afina12345!"
    When I navigate to the Book Store page
    Then I should see the books displayed in a grid
    And each book should have an image and a title
    And I should see the rows per page selector
    And I should see my username displayed

  Scenario: TC-B3 - Search book (public)
    When I search for "Learning JavaScript Design Patterns"
    Then the book title should be "Learning JavaScript Design Patterns"

  Scenario: TC-B4 - Search book (after login)
    Given I am logged in with username "afinapd" and password "Afina12345!"
    When I navigate to the Book Store page
    And I search for "Learning JavaScript Design Patterns"
    Then the book title should be "Learning JavaScript Design Patterns"
    And I should see my username displayed
