class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def con_to_kgs(self):
        return self.amount * value[self.currency]

    def __add__(self, other):
        total_add = self.con_to_kgs() + other.con_to_kgs()
        return f'{total_add}'


    def __sub__(self, other):
        total_sub = self.con_to_kgs() - other.con_to_kgs()
        return f'{total_sub}'

    def __mul__(self, other):
        total_mul = self.con_to_kgs() * other.con_to_kgs()
        return f'{total_mul}'

    def __truediv__(self, other):
        total_div = self.con_to_kgs() / other.con_to_kgs()
        return f'{total_div}'

money1 = Money(100, 'USD')
money2 = Money(5000, 'KGS')

value = {
    'KGS':1,
    'USD':89,
    'EUR':96,
    'RUB':1.2
}

print(money1 + money2)
print(money1 - money2)
print(money1 * money2)
print(money1 / money2)