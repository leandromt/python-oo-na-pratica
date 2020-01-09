from cash_machine import account_list, BankAccount


class AuthBankAccount:

    @staticmethod
    def authenticate(account_number, password):
        for account in account_list:
            if BankAccount.check_account_number() and BankAccount.check_password():
                print('Autenticado!')
                break
            else:
                print('Conta inválida!')
                break

    def has_bank_account
