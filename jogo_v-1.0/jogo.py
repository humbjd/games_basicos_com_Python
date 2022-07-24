import funções
import perguntas_respostas
from time import sleep

ini = 0

while True:
    print()
    inicio = input('\033[36mpress GO to enter\n').upper().strip()
    while inicio not in 'GO':
        inicio = input("\033[31mErro...\033[36mpress 'GO' to enter \n").upper().strip()
    sleep(1)
    funções.limpa()
    if inicio in 'GO':
        funções.menu()

        try:
            try:
                opcao = int(input('\033[32mSua escolha: \033[m'))
                while opcao > 5 or opcao < 0:
                    opcao = int(input('\033[31mErro..Valor indisponivel\n\033[32mSua escolha: \033[m'))
            except ValueError or TypeError or IndexError:
                opcao = int(input('\033[31mErro..Escolha um valor númerico\n\033[33mSua escolha: \033[m'))

            while True:

                if opcao == 0:
                    break

                elif opcao == 1:
                    perguntas_respostas.perg_esportes()

                elif opcao == 2:
                    perguntas_respostas.perg_musica()

                elif opcao == 3:
                    perguntas_respostas.perg_comida()

                elif opcao == 4:
                    perguntas_respostas.perg_novela()

                elif opcao == 5:
                    perguntas_respostas.perg_bebidas()

                sleep(1)
                ini += 1
                cont = str(input('\033[32mContinuar no mesmo tema?\033[34m[S/N] \033[m')).strip().upper()[0]
                while cont not in 'SsNn':
                    cont = str(input('\033[31mError...\n\033[32mContinuar no mesmo tema?'
                                     '\033[34m[S/N] \033[m')).strip().upper()[0]

                if cont in 'Ss':
                    sleep(0.9)
                    funções.limpa()

                else:
                    funções.limpa()
                    funções.menu()
                    try:
                        opcao = int(input('\033[32mSua escolha: \033[m'))
                        while opcao > 5 or opcao < 0:
                            opcao = int(input('\033[31mErro..Valor indisponivel\n\033[32mSua escolha: \033[m'))
                    except ValueError or TypeError or IndexError:
                        opcao = int(input('\033[31mErro..Escolha um valor númerico\n\033[33mSua escolha: \033[m'))
        except ValueError or TypeError or IndexError:
            print('\033[31mErro.. Tente novamente')
    break

print('\033[34mContabilizando seus pontos', end='')
funções.ponto()

perguntas_respostas.point()

if ini == 0:
    print('\033[30mQue pena não ter jogado :/')
elif ini >= 1:
    print('\033[33mGostou de ter jogado ? Se sim, joga denovo ai ;)')
sleep(15)

