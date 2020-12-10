# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

seconds_count = int(input('Введите время в секундах\n>>>'))
hours = seconds_count % 3600
if hours == 0:
    print(seconds_count, "секунд - это", seconds_count // 3600, "час", ": 00 мин : 00 сек")
else:
    minutes = hours % 60
    if minutes == 0:
        print(seconds_count, "секунд - это", seconds_count // 3600, "час",
              ":", (seconds_count % 3600) // 60, "мин", ": 00 сек")
    else:
        seconds = minutes % 60
        print(seconds_count, "секунд - это", seconds_count // 3600, "час", ":",
              (seconds_count % 3600) // 60, "мин", ":", seconds, "сек")
