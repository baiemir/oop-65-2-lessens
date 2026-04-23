import sqlite3

conn = sqlite3.connect('cinema.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        movie_id INTEGER NOT NULL,
        rating INTEGER CHECK(rating >= 1 AND rating <= 10),
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (movie_id) REFERENCES movies(id)
    )
''')

cursor.execute("DELETE FROM users")
cursor.execute("DELETE FROM movies")
cursor.execute("DELETE FROM reviews")

users_list = [('Ден',), ('Нурик',), ('Саня',), ('Широ',), ('Ронин',)]
cursor.executemany("INSERT INTO users (name) VALUES (?)", users_list)

movies_list = [
    ('Начало', 'Научная фантастика'),
    ('Темный рыцарь', 'Боевик'),
    ('Интерстеллар', 'Драма'),
    ('Джентльмены', 'Криминал'),
    ('Человек-паук', 'Приключения')
]
cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", movies_list)

reviews_list = [
    (1, 1, 10), (1, 2, 9),
    (2, 1, 8), (2, 3, 10),
    (3, 2, 7), (3, 4, 9),
    (4, 3, 10), (4, 5, 6),
    (5, 4, 8), (5, 1, 9), (5, 2, 10)
]
cursor.executemany("INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)", reviews_list)

conn.commit()
print("База данных успешно заполнена! \n")


def show_joins():
    print("1. Имя пользователя + Фильм + Оценка:")
    cursor.execute('''
        SELECT users.name, movies.title, reviews.rating
        FROM reviews
        JOIN users ON reviews.user_id = users.id
        JOIN movies ON reviews.movie_id = movies.id
    ''')
    for row in cursor.fetchall():
        print(f"{row[0]} оценил фильм «{row[1]}» на {row[2]}/10")

    print("\n2. ВСЕ фильмы (даже без отзывов):")
    cursor.execute('''
        SELECT movies.title, reviews.rating
        FROM movies
        LEFT JOIN reviews ON movies.id = reviews.movie_id
    ''')
    for row in cursor.fetchall():
        status = row[1] if row[1] else "Нет оценок"
        print(f"Фильм: {row[0]} | Оценка: {status}")


def show_aggregations():
    print("\n Статистика по оценкам:")
    cursor.execute('''
        SELECT 
            ROUND(AVG(rating), 2), 
            MAX(rating), 
            MIN(rating) 
        FROM reviews
    ''')
    avg_r, max_r, min_r = cursor.fetchone()
    print(f"Средняя оценка всех фильмов: {avg_r}")
    print(f"Максимальная оценка: {max_r}")
    print(f"Минимальная оценка: {min_r}")

show_joins()
show_aggregations()

conn.close()