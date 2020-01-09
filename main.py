from console import CacheMachineConsole, AuthBankAccountConsole
from utils import clear, header


def main():
    clear()
    header()
    AuthBankAccountConsole.is_auth()
    #CacheMachineConsole.call_operation()


if __name__ == '__main__':
    while True:
        main()
        input('Pressione <ENTER> para continuar...')
