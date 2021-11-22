import datetime

class Retirement:
    print('Social Security Full Retirement Age Calculator')

    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.ret_age = 0
        self.ret_month = 0
        
    def calculate_retirement_age(self, birth_year):
        birth_year = _validate_birth_year(birth_year)

        if birth_year <= 1937:
            self.ret_age = 65
            self.ret_month = 0
            return 65, 0
        elif birth_year == 1938:
            self.ret_age = 65
            self.ret_month = 2
            return 65, 2
        elif birth_year == 1939:
            self.ret_age = 65
            self.ret_month = 4
            return 65, 4
        elif birth_year == 1940:
            self.ret_age = 65
            self.ret_month = 6
            return 65, 6
        elif birth_year == 1941:
            self.ret_age = 65
            self.ret_month = 8
            return 65, 8
        elif birth_year == 1942:
            self.ret_age = 65
            self.ret_month = 10
            return 65, 10
        elif 1943 <= birth_year <= 1954:
            self.ret_age = 66
            self.ret_month = 0
            return 66, 0
        elif birth_year == 1955:
            self.ret_age = 66
            self.ret_month = 2
            return 66, 2
        elif birth_year == 1956:
            self.ret_age = 66
            self.ret_month = 4
            return 66, 4
        elif birth_year == 1957:
            self.ret_age = 66
            self.ret_month = 6
            return 66, 6
        elif birth_year == 1958:
            self.ret_age = 66
            self.ret_month = 8
            return 66, 8
        elif birth_year == 1959:
            self.ret_age = 66
            self.ret_month = 10
            return 66, 10
        else:
            self.ret_age = 67
            self.ret_month = 0
            return 67, 0

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def _validate_age_month(month):
        month = int(month)

        if month < 0 or month > 11:
            raise ValueError(f'Age month "{month}" must be between 0 and 11')

        return month


    def _validate_age_year(year):
        year = int(year)

        if year < 65 or year > 67:
            raise ValueError(f'Age year "{year}" must be between 65 and 67')

        return year


    def validate_birth_month(month):
        month = int(month)

        if month < 1 or month > 12:
            raise ValueError(f'Birth month "{month}" must be between 1 and 12')

        return month


    def validate_birth_year(year):
        year = int(year)

        if year < 1900:
            raise ValueError(f'Birth year "{year}" must be no earlier than 1900')
        elif year >= 3000:
            raise ValueError(f'Birth year "{year}" must be earlier than 3000')

        return year

    def get_retage(self):
        return self.ret_age

    def get_retmonth(self):
        return self.ret_month