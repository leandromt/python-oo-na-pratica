class BankAccount:
    def __init__(self, account_number, name, password, value, admin):
        self.account_number = account_number
        self.name = name
        self.password = password
        self.value = value
        self.admin = admin

    def check_account_number(self, account_number):
        return account_number == self.account_number

    def check_password(self, password):
        return password == self.password

class CacheMachine:

    def __init__(self, money_slips):
        self.money_slips = money_slips
        self.money_slips_user = {}
        self.value_remaining = 0

    def withdraw(self, value):

        self.value_remaining = value

        if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
            money_slips_user['100'] = value_int // 100
            value_int = value_int - value_int // 100 * 100

        if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
            money_slips_user['50'] = value_int // 50
            value_int = value_int - value_int // 50 * 50

        if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
            money_slips_user['20'] = value_int // 20
            value_int = value_int - value_int // 20 * 20

        if value_int != 0:
            print('O caixa não tem cédulas disponíveis para este valor')
        else:
            for money_bill in money_slips_user:
                money_slips[money_bill] -= money_slips_user[money_bill]
            save_money_slips()
            print('Pegue as notas:')
            print(money_slips_user)

accounts_list = [
    BankAccount('0001-01', 'Fulano de Tal', '123456', 100, False),
    BankAccount('0002-02', 'Sicrano de Tal', '123456', 200, False),
    BankAccount('0003-03', 'Beltrano de Tal', '123456', 300, True),
    BankAccount('0004-04', 'Sucano de Tal', '123456', 400, False)
]