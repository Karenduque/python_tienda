Feature: Buy product
@test
Scenario: Buy product in saucedemo
    Given I am on the saucedemo Products page
    When I am looking for the product Sauce Labs Bolt T-Shirt
    When I click add to cart button Sauce Labs Bolt T-Shirt
    Then Sauce Labs Bolt T-Shirt product is added to cart