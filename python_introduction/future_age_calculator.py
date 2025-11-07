# first ask user ther age 
# second assume current year is 2023 and
# add that year in users age 
# print(In 2050, you will be {})
this_year = 2023
calc_year = 2050
user_age = float(input("How old are you? ")) 
In_2050_user_age = (calc_year - this_year) + user_age
result = "In 2050, you will be " + str(In_2050_user_age) + " years old."
print(result)