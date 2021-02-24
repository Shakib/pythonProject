Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange HRM Homeage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User muset successfully login to the Dashboard page


    Scenario Outline: Login to orangeHRM with multiple parameters
      Given I launch chrome browser
      When I open orange HRM homepage
      And Enter username "<username>" and password "<password>"
      And click on login button
      Then User must successfully login to the Dashboard page

      Examples:
      |username|password|
      |Admin   |admin123|
      |admin123|admin123|
      |adminxyz|admin123|
      |Admin   |admin123|