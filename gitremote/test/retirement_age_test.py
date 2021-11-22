import pytest
from pytest_bdd import scenario, given, when, then, parsers
from FullRetirementAge import Retirement


@scenario('../features/retirement_age.feature', 'Get Retirement Age')
def test_age():
    pass


@pytest.fixture
@given(parsers.parse('I input the {year} and the month {month}'))
def year_month_input(year, month):
    Retirement(year, month)


@when("I calculate retirement age")
def calc_ret_age():
    Retirement.calculate_retirement_age(Retirement.get_year())


@then(parsers.parse('retirement age is {retire_years} and {retire_months} months'))
def retirement_age(retire_years, retire_months):
    assert Retirement.get_retage() == int(retire_years)
    assert Retirement.get_retmonth() == int(retire_months)
