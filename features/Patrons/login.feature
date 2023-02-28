Feature: Login in saucedemo
@test
Scenario Outline: Login in saucedemo
    Given I am on the saucedemo loginpage
    When I enter username "<username>" and I enter password "<pwd>"
    When I click login button
    Then I am logged in

    Examples:
      | username             | pwd     |
      | standard_user        | secret_sauce|

@test
Scenario: Buy product in saucedemo and logout
    Given I am on the saucedemo Products page
    When I am looking for the product Sauce Labs Bolt T-Shirt
    When I click add to cart button Sauce Labs Bolt T-Shirt
    When I click in menu button
    When I click in link logout

