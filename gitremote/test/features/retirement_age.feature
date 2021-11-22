Feature: Retirement Age Calculator
  I want to calculate age of retirement
  Examples:
      | year | month | retire_years | retire_months |
      | 1943 | 1     | 66        | 0          |
      | 1955 | 1     | 66        | 2          |
      | 1956 | 1     | 66        | 4          |
      | 1957 | 1     | 66        | 6          |
      | 1958 | 1     | 66        | 8          |
      | 1959 | 1     | 66        | 10         |
      | 1960 | 1     | 67        | 0          |
  Scenario Outline: Get Retirement Age
    Given I was born in the <year> and the month <month>
    When I calculate retirement age
    Then retirement age is <retire_years> and <retire_months> months