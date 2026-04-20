import sqlite3

conn = sqlite3.connect('store.db')
cursor = conn.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS store (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (50) NOT NULL,
        price INTEGER NOT NULL,
        quantity INTEGER NOT NULL
        )
''')
#conn.commit()

# def create_my_user(name, price, quantity):
#     cursor.execute(
#     'INSERT INTO store (name, price, quantity) VALUES (?, ?, ?)',
#     (name, price, quantity)
#     )
#     #conn.commit()
#     print('Пользователь добавлен!')
#
# create_my_user('Мандарин', 250, 15)
# create_my_user('Яблоко',180 , 10)

# def read_products():
#     cursor.execute('''SELECT name, price FROM store''')
#
#     products = cursor.fetchall()
#
#     print('---Товар из магазина---')
#     for item in products:
#         print(item[0], item[1])
#         #print(item[0], item[1], item[2])
#
# read_products()

def update_products(new_price, product_id):
    cursor.execute('UPDATE store SET price=? WHERE id=?', (new_price, product_id))
    conn.commit()

    print(f'Цена товара с ID {product_id} успешно изменена на {new_price}')

update_products(300, 1)
conn.commit()

def delete_products(product_id):
    cursor.execute('DELETE FROM store WHERE id=?', (product_id,))
    conn.commit()
    print(f'Товар с ID {product_id} успешно удалена')

delete_products(6)
delete_products(5)
delete_products(4)
delete_products(3)