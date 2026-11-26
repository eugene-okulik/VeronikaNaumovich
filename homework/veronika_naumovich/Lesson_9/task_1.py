import datetime
my_time = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime (my_time, '%b %d, %Y - %T')

print(python_date.strftime('%B'))
human_date = python_date.strftime('%d.%m.%Y, %R')
print(human_date)
