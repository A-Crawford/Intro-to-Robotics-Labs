num_days = int(input("Enter number of days: "))
years = 0
weeks = 0
days = 0

if (num_days >= 365):
    years = round((num_days / 365), 0)
    num_days = num_days - (years * 365)

if (num_days >= 7):
    weeks = round((num_days / 7), 0)
    num_days = num_days - (weeks * 7)

days = num_days

print(f"Years: {years}, WWeeks: {weeks}, Days: {days}")
