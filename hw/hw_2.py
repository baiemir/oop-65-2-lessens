class Hero:
    def __init__(self, name, lvl, health, strength):
        self.name = name
        self.lvl = lvl
        self.health = health
        self.strength = strength

class Warrior(Hero):
    def __init__(self, name, lvl, health, strength, stamina):
        super().__init__(name, lvl, health, strength)
        self.stamina = stamina

    def greet(self):
        return f'Привет мое имя {self.name}, мой уровень {self.lvl}'

    def attack(self):
        return f'{self.name} наносит урон мечом!!!'

    def rest(self):
        return f'{self.name} отдыхает и восстонавливает здоровье'

class Mage(Hero):
    def __init__(self, name, lvl, health, strength, mp):
        super().__init__(name, lvl, health, strength)
        self.mp = mp

    def greet(self):
        return f'Привет мое имя {self.name}, мой уровень {self.lvl}'

    def attack(self):
        return f'{self.name}: На небесах и на земле лишь я один достойный. Техника пустоты Фиолетовый!!!'

    def rest(self):
        return f'{self.name} отдыхает и восстонавливает здоровье'

class Assassin(Hero):
    def __init__(self, name, lvl, health, strength, stealth):
        super().__init__(name, lvl, health, strength)
        self.stealth = stealth

    def greet(self):
        return f'Привет мое имя {self.name}, мой уровень {self.lvl}'

    def attack(self):
        return f'{self.name} наносит урон йо-йо из под тишка!!!'

    def rest(self):
        return f'{self.name} отдыхает и восстонавливает здоровье'

guts = Warrior('Guts', 20, 100, 100, 100)
gojo = Mage('Gojo', 20, 100, 100, 100)
killua = Assassin('Killua', 20, 100, 100, 100)

# print(guts.greet(), guts.attack(), guts.rest())
# print(gojo.greet(), gojo.attack(), gojo.rest())
# print(killua.greet(), killua.attack(), killua.rest())

import random

heroes = [guts, gojo, killua]


print('Выберите героя:')
for i, hero in enumerate(heroes, 1):
    print(f'{i}. {hero.name}')

choice = int(input("Введите номер (1-3): ")) -1
user_hero = heroes[choice]

enemy_hero = random.choice(heroes)

print(f'\nВы выбрали:'
      f' {user_hero.name}')
print(f'Противник:'
      f'{enemy_hero.name}')

user_type = user_hero.name
enemy_type = enemy_hero.name

if user_hero == enemy_hero:
    print("Ничья ! Силы равны.")

elif (user_type == Warrior and enemy_type == Assassin) or \
        (user_type == Assassin and enemy_type == Mage) or \
        (user_type == Mage and enemy_type == Warrior):
    print(f'{user_type} победил!!!')

else:
    print(f'{enemy_type} победил!!!')

