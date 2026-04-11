class Hero:

    # Конструктор класс
        def __init__(self, name, hp, lvl):
            # Атрибуты класс
            self.name_hero = name
            self.hp_hero = hp
            self.lvl_hero = lvl
        # Метод класса
        def action(self):
            return f'{self.name_hero} hero based action!!!'

# Обьет \ экземпляр на основе класса
itachi = Hero("Itachi", 100, 10)
sasuke = Hero("Sasuke", 100, 10)

# print(itachi.name_hero)
# print(itachi.hp_hero)
# print(itachi.lvl_hero)
print(itachi.action())