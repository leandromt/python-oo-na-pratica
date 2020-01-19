import getpass

from auth import AuthBankAccount


class AuthBankAccountConsole:

    @staticmethod
    def is_auth():
        account_typed = input('Digite sua conta: ')
        password_typed = getpass.getpass('Digite sua senha: ')

        return AuthBankAccount.authenticate(account_typed, password_typed)


class CacheMachineConsole:

    @staticmethod
    def call_operation():
        option_typed = CacheMachineConsole.__get_menu_option_typed()
        CacheMachineOperation.do_operation(option_typed)

    @staticmethod
    def __get_menu_option_typed():
        print('%s - Saldo' % CacheMachineOperation.OPERATION_SHOW_BALANCE)
        print('%s - Saque' % CacheMachineOperation.OPERATION_WITHDRAW)
        return input('Escolha uma das opções acima: ')


class CacheMachineOperation:
    OPERATION_SHOW_BALANCE = '1';
    OPERATION_WITHDRAW = '2';

    @staticmethod
    def do_operation(option):
        if option == CacheMachineOperation.OPERATION_SHOW_BALANCE:
            ShowBalanceOperation.do_operation()
        elif option == CacheMachineOperation.OPERATION_WITHDRAW:
            WithDrawOperation.do_operation()
        else:
            OperationNotFound.do_operation()


class ShowBalanceOperation:

    @staticmethod
    def do_operation():
        bank_account = AuthBankAccount.bank_account_authenticated
        print('Seu saldo é %s' % bank_account.value)


class WithDrawOperation:

    @staticmethod
    def do_operation():
        print('Sacar!')


class OperationNotFound:

    @staticmethod
    def do_operation():
        print('Opção Inválida!')
