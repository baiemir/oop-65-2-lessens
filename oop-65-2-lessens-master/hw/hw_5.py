from faker import Faker

# Faker — библиотека для генерации фальшивых данных.
# подходит на все случаи жизни: тестирование кода,
# заполнение баз данных для стресс-тестов, анонимизация данных.
# Для всего этого используют Faker.


# Инициализация (по умолчанию на английском)
fake = Faker()

# Генерация различных данных
print(fake.name())      # Случайное имя (например, "John Doe")
print(fake.address())   # Случайный адрес
print(fake.email())     # Случайный email
print(fake.text())      # Случайный текст

# Инициализация для русского языка
fake = Faker('ru_Ru')

print(fake.name())      # Например, "Иванов Иван"
print(fake.address())   # Адрес в РФ
print(fake.email())     # Телефон в формате РФ

# Инициализация для японского языка
fake = Faker('ja_Jp')

# Создаем список из 5 случайных пользователей
user = []
for _ in range(5): # Заставляет программу пвоторить действие 5 раз если бы мы хотели видеть номер
    # пользователя то написали бы for i in range(5)

    users = {
    'fake_name': fake.name(),
     'fake_address': fake.address(),
     'fake_email': fake.email(),
     'fake_phone_number': fake.phone_number(),
        'fake_text': fake.word()
    }
    user.append(users) # Это ключевой момент в работе со списками в Пайтон.
    # В коде отвечает за сохранение каждого созданного словаря в общий список

print(user)

# Сгенерирует 10 уникальных email-адресов
for _ in range(10):
    print(fake.unique.email())      # Если нам нужны неповторяющиеся данные используем: .unique
    print(fake.unique.name())

# Популярные методы Faker

# fake.name()     #ФИО
# fake.address()  # Адресс
# fake.email()    # Емайл
# fake.phone_number() # Номер телефона
# fake.date()     # Дата
# fake.date_time()    # Фейковое время
# fake.company()  # Название комании
# fake.text()     # Текст
# fake.word()     #  Случайное слово
# fake.sentence() # Предложение
