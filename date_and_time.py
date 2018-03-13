from datetime import datetime

# Получение текущей даты и времени
now = datetime.now()
print(now)

# Получение части даты
current_year = now.year
current_month = now.month
current_day = now.day
print('%s : %02d' % (current_day, current_month))

now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.time())


# Формат даты, замена строк: mm/dd/yyyy
now = datetime.now()
print('%02d/%02d/%04d' % (now.month, now.day, now.year))


# Формат времени: hh:mm:ss
now = datetime.now()
print('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
# mm/dd/yyyy hh:mm:ss.
print('%02d/%02d/%04d %02d:%02d:%02d' % (now.month, now.day, now.year, now.hour, now.minute, now.second))



