# Создание абстрактного класса
from abc import ABC, abstractmethod
class Hero(ABC):

    # Атрибуты класса Hero
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self._health = health
        self.strength = strength

    # Методы класса

    def greet(self):
        pass

    def rest(self):
        self._health += 1
        pass

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        return f'Привет я {self.name}, мой уровень {self.lvl}.'

    def rest(self):
        self._health += 1
        return f'{self.name} отдыхает увеличвается {self._health} на 1'

    def attack(self):
        return f'{self.name} атакует мечом.'

class Mage(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        return f'Привет я {self.name}, мой уровень {self.lvl}.'

    def rest(self):
        self._health += 1
        return f'{self.name} отдыхает увеличвается {self._health} на 1'

    def attack(self):
        return f'{self.name} атакует фиолетовым.'

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength):
        super().__init__(name, lvl, health, strength)

    def greet(self):
        return f'Привет я {self.name}, мой уровень {self.lvl}.'

    def rest(self):
        self._health += 1
        return f'{self.name} отдыхает увеличвается {self._health} на 1'

    def attack(self):
        return f'{self.name} атакует из-под тишка.'

guts = Warrior('Guts', 1, 100, 100)
gojo = Mage('Gojo', 1, 100, 100)
killua = Assassin('Killua', 1, 100, 100)

print(guts.greet(), guts.attack(), guts.rest())
print(gojo.greet(), gojo.attack(), gojo.rest())
print(killua.greet(), killua.attack(), killua.rest())