import pytest
from pytest_bdd import scenario, given, when, then, parsers
from FullRetirementAge import Retirement


@scenario('../features/invalid_month.feature', 'Invalid Month')
def test_invalid_month():
    pass


@pytest.fixture
@given(parsers.parse('I input the {year} and the invalid month {month}'))
def year_invalid_month_input(year, month):
    Retirement(year, month)


@when("I input a non-int value")
def input_invalid_val():
    Retirement.validate_birth_month(Retirement.get_month())


@then(parsers.parse('raises ValueError'))
def invalid_month_return():
    pytest.raises(ValueError)
