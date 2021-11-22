Feature: Retirement Age Calculator
  I want to calculate age of retirement
  Examples:
      | year | month | returns |
      | 1999 | "test" | ValueError |

  Scenario: Invalid Month
    Given I was born in the <year> and the month <month>
    When I input a non-int value for the month
    Then raises ValueError