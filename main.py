# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Life limitation
whole_month = 90 * 12
whole_week = 90 * 52
whole_day = 90 * 365

# print(f"whole_month = {whole_month}")
# print(f"whole_week = {whole_week}")
# print(f"whole_day = {whole_day}")

# My Time
my_month = int(age) * 12
my_week = int(age) * 52
my_day = int(age) * 365

# print(f"my_month = {my_month}")
# print(f"my_week = {my_week}")
# print(f"my_day = {my_day}")

# Time Limit
x = whole_day - my_day
y = whole_week - my_week
z = whole_month - my_month

print(f"You have {x} days, {y} weeks, and {z} months left.")

#Shorten

years_remaining = 90 - int(age)
month_remaining = years_remaining * 12
week_remaining = years_remaining * 52
day_remaininng = years_remaining * 365

print(f"You have {day_remaininng} days, {week_remaining} weeks, and {month_remaining} months left.")

