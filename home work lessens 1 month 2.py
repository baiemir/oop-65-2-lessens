class Hero:
    def __init__(self, name, lvl, health, strength):
        self.name_hero = name
        self.lvl_hero = lvl
        self.health_hero = health
        self.strength_hero = strength
    def greet(self):
        return  f'Привет, я {self.name_hero}, мой уровень {self.lvl_hero}'
    def attack(self):
        return f'{self.name_hero} наносит удар! уменьшает силу героя на 1'
    def reset(self):
        return f'{self.name_hero} отдыхает... увеличивает здоровье героя на 1'
guts = Hero('Guts', 250, 2000, 99)
print(guts.greet(), (guts.attack()), (guts.reset()), sep='\n')
