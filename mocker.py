import random


id_device = 102
id_location = 41

hour = "12.00.00.000000 PM"
month_from = 1
month_to = 5
year = 2019

iterator = 31 # measure every *iterator* days

top_value_ranges= [28, 25, 30, 35, 62, 74, 84, 72, 45, 38, 38, 33]
bottom_value_ranges = [25, 22, 25, 30, 60, 70, 80, 68, 40, 35, 35, 30]
max_diff = 4

base = "INTO measurements (id_device, date_time, value, id_location) VALUES"
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
numb_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# print sql query
print("INSERT ALL")
for month in range(month_from, month_to+1):
    values = []

    # create random values
    for i in range(0, numb_of_days[month-1]):
        values.append(random.randint(bottom_value_ranges[month-1], top_value_ranges[month-1]))

    # decrease difference between values
    for i in range(1, len(values)):
        if abs(values[i]-values[i-1]) > max_diff:
            values[i] = (values[i] + values[i-1])/2

    for i in range(0, len(values), iterator):
        if i+1 < 10:
            today = "0" + str(i+1)
        else:
            today = i+1

        print("{} ({}, '{}-{}-{} {}', {}, {})" .format(base, id_device, today, months[month-1], year, hour, values[i], id_location))
print("SELECT * FROM dual;")