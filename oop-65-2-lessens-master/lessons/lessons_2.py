# Тема: Принципы ООП - Наследования, Полиморфизм. Гит - коммиты, создание веток, git push
from symtable import Class

from lessons.lessons_1 import itachi


# Наследование

# Родительский\Супер класс
class Hero:
    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl

    def action(self):
        return f'{self.name} based action!!'

itachi = Hero('itachi', 100, 10)

# Дочерний класс
class MageHero(Hero):
    pass

    def __init__(self, name, hp, lvl, mp):

        # Добавляем новый атрибук MP
        super().__init__(name, hp, lvl)
        self.mp = mp

    def action(self):
        print(f'i`m {self.name} this my base action!!! MY MP {self.mp}')
sasuke = MageHero('sasuke', 100, 10, 100)

# print(itachi.action())
# print(sasuke.action())


class Fly:
    def action(self):
        print('Fly')

class Swim:
    def action(self):
        print('Swim')

class Animal(Swim, Fly):
    pass

duck = Animal()

duck.action()
