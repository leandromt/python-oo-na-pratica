import getpass

from auth import AuthBankAccount


class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        account_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')
        AuthBankAccount.authenticate(account_typed, password_typed)


class CacheMachineConsole:

    @staticmethod
    def call_operation():
        option_typed = CacheMachineConsole.get_menu_option_typed()
        CacheMachineOperation.do_operation(option_typed)

    @staticmethod
    def get_menu_option_typed():
        print('1 - Saldo')
        print('2 - Saque')
        return input('Escolha uma das opções acima: ')


class CacheMachineOperation:

    @staticmethod
    def do_operation(option):
        if option == '1':
            ShowBalanceOperation.do_operation()
        elif option == '2':
            WithDrawOperation.do_operation()
        else:
            OperationNotFound.do_operation()


class ShowBalanceOperation:

    @staticmethod
    def do_operation():
        print('Mostrar saldo!')


class WithDrawOperation:

    @staticmethod
    def do_operation():
        print('Sacar!')


class OperationNotFound:

    @staticmethod
    def do_operation():
        print('Opção Inválida!')
