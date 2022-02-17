import re
def isLeapYear(year):
    (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def isValidDate(date):
    dateRegex = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    mo = dateRegex.search(date)
    try:
        day, month, year = int(mo.group(1)), int(mo.group(2)), int(mo.group(3))
    except AttributeError:
        return False
    # Check year
    if year < 1000 or year > 2999:
        return False
    # Check month
    elif month < 1 or month > 12:
        return False
    # Check day
    elif day < 1:
        return False
    longMonths = [1,3,5,7,8,10,12]
    shortMonths = [4,6,9,11]
    if month in longMonths:
        if day > 31:
            return False
    elif month in shortMonths:
        if day > 30:
            return False
    else:
        if isLeapYear(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    return True

print(isValidDate("01/01/2001"))
print(isValidDate("27/22/2000"))
print(isValidDate("27/22/999"))
