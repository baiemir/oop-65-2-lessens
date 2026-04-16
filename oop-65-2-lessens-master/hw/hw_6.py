# Задание 1:
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def is_admin(func):
    def wrapper(user, *args, **kwargs):
        print(f'Проверка роли {user.name}')
        if user.role == 'admin':
            return func(user, *args, **kwargs)
        else:
            print(f'У вас {user.name} нет досутпа')
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

admin_acc = User('r0nin', 'admin')
user_acc = User('Den', 'user')

delete_video(user_acc)

# Задание 2:
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = round(end_time - start_time, 1)
        print(f'Время выполнения: {duration} секунд')
        return result
    return wrapper

@timer
def download_video():
    time.sleep(5)
    print("Видео загружено")

download_video()

