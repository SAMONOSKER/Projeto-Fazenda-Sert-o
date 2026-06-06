from cadastrosUsuarios import usuarios
from menu import  menurebanho, menucadas, menugerenciamento
from cadastroanimal import bovi, capri, ovino, suino, equino, lista

relatorio = []





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
                equino()

            elif escolha == '0':
                break

            else:
                print('Opção inválida!')

        elif escolha == '2':
            lista()

#         elif escolha == '3':
#             busca = input('Digite o brinco do animal: ')
#             encontrado = False
#
#             for v in animais:
#                 if v[1] == busca:
#                     encontrado = True
#                     print('=' * 5, 'Animal Encontrado', '=' * 5)
#
#                     novoTipo = input('Novo tipo: ')
#                     novoStatus = input('Novo status: ')
#
#                     v[0] = novoTipo
#                     v[2] = novoStatus
#
#                     print('Animal Atualizado!')
#             if not encontrado:
#                 print('Animal não encontrado!')
#
#         elif escolha == '4':
#             busca = input('Digite o brinco do animal: ')
#             encontrado = False
#
#             for v in animais:
#                 if v[1] == busca:
#                     encontrado = True
#
#                     animais.remove(v)
#                     print('Animal removido!')
#                     break
#             if not encontrado:
#                 print(f"\nO brinco {busca} não foi encontrado!")
#
#         elif escolha == '5':
#             if len(animais) == 0:
#                 print('Nenhum animal cadastrado!')
#
#             else:
#                 print('=' * 10, 'Lista de animais', '=' * 10)
#
#                 for v in animais:
#                     print('Tipo:', v[0])
#                     print('Brinco:', v[1])
#                     print('Status:', v[2])
#
#         elif escolha == '0':
#             print('Encerrando o gerenciamento do rebanho...')
#             break
#
#         else:
#             print('Opção inválida')
#
def loginn():
    print()
    print('=' * 10, 'Login', '=' * 10)

    usuario = input('Digite seu nome de usuário: ')
    if not usuarios:
        print('Usuário não cadastrados.')
    else:
        encontrado = False
        for v in usuarios:
            if v['nome'] == usuario:
                encontrado = True
                senha = input('Digite sua senha: ').lower()

        if encontrado == False:
            print('Usuário não cadastrado!')

        logado = False

        for i in usuarios:
            if i['nome'] == usuario and i['senha'] == senha:
                logado = i

            if logado:
                while True:
                    if logado['ID'] == 'ADM':
                        print(f'\n========== Bem-Vindo {logado['nome']} ==========\n')

                    menugerenciamento()
                    escolha = input('Digite sua opção: ')

                    if escolha == '1':
                        rebanho()