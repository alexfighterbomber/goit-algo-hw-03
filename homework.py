from datetime import datetime
import random, re

def get_days_from_today(date: str)-> int:      # розрахунок кількості днів між date та поточною датою
    current_date = datetime.today().date()
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()   # рядок в формат datetime
    except ValueError:
        return 'Невірний формат дати. Використовуйте "РРРР-ММ-ДД"'
    return (current_date - target_date).days

def get_numbers_ticket(min=1, max=36, quantity=5):  # отримання quantity довільних унікальних чисел з діапазону min - max
    if min < 1 or min > max-quantity or quantity > max-min or quantity < 1 or max > 1000 or min > max:
        return "Невірні вхідні дані!"
    numbers = set() #створюємо множину
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max)) # додаємо в неї довільні числа поки не наберемо кількість quantity
    sorted_numbers = sorted(numbers)          # перетворюємо на сортований список
    return sorted_numbers

def normalize_phone(phone_number): # нормалізація телефонних номерів
    return "+380" + re.sub(r"\D*", "", phone_number)[-9:] # залишаємо тількі останні 9 цифр номера та додаємо префікс: +380

print(get_days_from_today("2021-10-09"))

print(get_numbers_ticket(1,49,6))

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)