Feature: Logout saucedemo
@test
Scenario: Logout saucedemo
    Given I am logged on the saucedemo
    When I click in menu button
    and I click in link logout
    Then return to login page