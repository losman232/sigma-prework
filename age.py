#  program to calculate age in years

# import date from data and time module
from datetime import date

# birthday in (yyyy,mm,dd)format
birthday = date(1996, 2, 3)
# get todays date
today = date.today()
# calculate age by subtracting year from birthday from current year
age = today.year - birthday.year

# display age
print(age, "years")
