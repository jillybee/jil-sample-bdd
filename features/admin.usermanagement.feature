Feature: Admin_User_Management
  Scenario: Navigate_to_System_Users_page
    Given I login to the application
    When I click "Admin" menu
      And I click "User Management" menu
    Then "SYSTEM_USERS_PAGE" page is displayed

  @wip
  Scenario: Navigate_to_System_Users_page
    Given "System Users" page is displayed
    When I click "Add" button
    Then "Add User" page is displayed