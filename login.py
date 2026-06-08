from cadastrosUsuarios import usuarios
from menu import menurebanho, menucadas, menugerenciamento
from cadastroanimal import bovi, capri, ovino, suino, equinno, lista, atualizaranimal, removeranimal,relatoriogeral
from menucliente import menu_principal, menu_loja, listar_animais
from Lojadocliente import listar_animais, menu_loja
from produtosadm import menuprodutos





def rebanho():

    while True:

        menurebanho()
        escolha = input('Digite sua opção: ')

        if escolha == '1':
            menucadas()
            escolha = input('Digite sua opção: ')

            if escolha == '1':
                bovi()

            elif escolha == '2':
                capri()

            elif escolha == '3':
                ovino()

            elif escolha == '4':
                suino()

            elif escolha == '5':
                equinno()

            elif escolha == '0':
               break

            else:
                print('Opção inválida!')

        elif escolha == '2':
            lista()

        elif escolha == '3':
            atualizaranimal()

        elif escolha == '4':
            removeranimal()

        elif escolha == "0":
            break

        # elif escolha == '3':

def loginn():
    print()
    print('=' * 10, 'Login', '=' * 10)

    usuario = input('Digite seu nome de usuário: ')

    if not usuarios:
        print('Usuário não cadastrado.')
        return

    senha = input('Digite sua senha: ').lower()

    logado = False

    for i in usuarios:
        if i['nome'] == usuario and i['senha'] == senha:
            logado = i
            break

    if not logado:
        print('Usuário ou senha inválidos!')
        return

    if logado['ID'] == 'ADM':

        while True:
            print(f"\n========== Bem-Vindo {logado['nome']} ==========\n")

            menugerenciamento()
            escolha = input('Digite sua opção: ')

            if escolha == '1':
                rebanho()

            elif escolha =='2':
                menuprodutos()

            elif escolha == '3':
                relatoriogeral()


            elif escolha == '0':
                return

    elif logado['ID'] == 'CLI':

        while True:
            print(f"\n========== Bem-Vindo {logado['nome']} ==========\n")

            menu_principal()
            escolha = input('Digite sua opção: ')

            if escolha == '1':
                listar_animais()
                menu_loja()

            elif escolha == '0':
                return






