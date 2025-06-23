#  calculate age in years

from datetime import date

birthday = date(1996, 2, 3)
today = date.today()
age = today.year - birthday.year


print(age, "years")
