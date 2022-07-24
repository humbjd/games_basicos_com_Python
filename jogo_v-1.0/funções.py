
def ponto():
    from time import sleep
    for c in range(0, 5):
        print('.', end='', flush=True)
        sleep(0.5)
    print()


def menu():
    from time import sleep
    print('\033[33m     Temas \033[m')
    temas = ('| 1 - Esportes',
             '| 2 - Musica',
             '| 3 - Comida',
             '| 4 - Novela',
             '| 5 - Bebidas',
             '| 0 - Sair'
             )
    print('\033[34m -' * 10)
    for item in temas:
        print(f'\033[93m{item:<20}|', '\033[34m')
        sleep(0.5)

    print(' -' * 10, '\033[m')


def limpa():
    import os
    return os.system('cls')

