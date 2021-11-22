Feature: Retirement Age Calculator
  I want to calculate age of retirement
  Examples:
      | year | month | returns |
      | "test" | 1 | ValueError |

  Scenario: Invalid Year
    Given I was born in the <year> and the month <month>
    When I input a non-int value for the year
    Then raises ValueError