class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f'{self.name} готов к бою!!!'

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f'{self.name} кастует заклинание. MP {self.mp}'

class WarriorHero(MageHero):
    def __init__(self, name, lvl, hp, stamina):
        super().__init__(name, lvl, hp, stamina)
        self.stamina = stamina

    def action(self):
        return f'{self.name} рубит мечом! Уровень {self.lvl}'

class BankAccount:
    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balancebalance = balance # (_) Защищенный
        self.__password = password # (__) Приватный
        self.bank_name = bank_name

    def login(self, password):
        self._password == password


