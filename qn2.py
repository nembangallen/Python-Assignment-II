"""
2. Write an if statement to determine whether a variable holding a year
is a leap year.
"""


def is_leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if(year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = 1996
if(is_leap_year(year)):
    print(str(year) + ' is a Leap Year.')
else:
    print(str(year) + ' is not a Leap Year.')
