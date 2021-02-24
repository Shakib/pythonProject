Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM home page
    Given Launch chrome browser
    When Open orange hrm homepage
    Then Verify that the logo present on page
    And Close browser
