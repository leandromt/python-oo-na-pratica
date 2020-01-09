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


account_list = [
    BankAccount('0001-01', 'Fulano de Tal', '123456', 100, False),
    BankAccount('0002-02', 'Sicrano de Tal', '123456', 200, False),
    BankAccount('0003-03', 'Beltrano de Tal', '123456', 300, True),
    BankAccount('0004-04', 'Sucano de Tal', '123456', 400, False)
]