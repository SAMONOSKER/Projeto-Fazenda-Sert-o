from cadastrosUsuarios import usuarios
from cadastroanimal import menucadas
from cadastroanimal import animais
from cadastroanimal import statusbov, lactabov, engordabov, vendabov, tratamentobov, vicinabov
from cadastroanimal import statuscapri, engordacapri, vendacapri, tratamentocapri, vacinacapri



def bovi():
    while True:
        statusbov()
        escolha = input('\nInforme sua opção: ')
        if escolha == '1':
            lactabov()

        elif escolha == '2':
            engordabov()

        elif escolha == '3':
            vendabov()

        elif escolha == '4':
            tratamentobov()

        elif escolha == '5':
            vicinabov()

        elif escolha == '0':
            break

        else:
            print('\nOpção inválida! Tente novamente.')

def capri():
    while True:
        statuscapri()
        escolha = input('\nInforme sua opção: ')

        if escolha == '1':
            engordacapri()

        elif escolha == '2':
            vendacapri()

        elif escolha == '3':
            tratamentocapri()

        elif escolha == '4':
            vacinacapri()

        elif escolha == '0':
            break

        else:
            print('\nOpção inválida! Tente novamente.')



def rebanho():

    while True:
        print()
        print('=' * 10, 'Gerenciamento do Rebanho', '=' * 10)
        print('[1] - Cadastrar animal')
        print('[2] - Buscar animal')
        print('[3] - Atualizar animal')
        print('[4] - Remover animal')
        print('[5] - Listar animais')
        print('[0] - Sair')

        escolha = input('Digite sua opção: ')

        if escolha == '1':
            menucadas()
            escolha = input('Digite sua opção: ')

            if escolha == '1':
                bovi()

            elif escolha == '2':
                capri()





        elif escolha == '2':
            print()
            print('=' * 10, 'Buscar animal', '=' * 10)
            buscar = input('Digite o número do brinco: ')

            encontrado = False

            for v in animais:
                if v[1] == buscar:
                    encontrado = True
                    print()
                    print('=' * 5, 'Animal Encontrado', '=' * 5)
                    print(f'Tipo: {v[0]} || Brinco: {v[1]} || Status: {v[2]}')
            if not encontrado:
                print('Animal não Encontrado.')

        elif escolha == '3':
            busca = input('Digite o brinco do animal: ')
            encontrado = False

            for v in animais:
                if v[1] == busca:
                    encontrado = True
                    print('=' * 5, 'Animal Encontrado', '=' * 5)

                    novoTipo = input('Novo tipo: ')
                    novoStatus = input('Novo status: ')

                    v[0] = novoTipo
                    v[2] = novoStatus

                    print('Animal Atualizado!')
            if not encontrado:
                print('Animal não encontrado!')

        elif escolha == '4':
            busca = input('Digite o brinco do animal: ')
            encontrado = False

            for v in animais:
                if v[1] == busca:
                    encontrado = True

                    animais.remove(v)
                    print('Animal removido!')
                    break
            if not encontrado:
                print(f"\nO brinco {busca} não foi encontrado!")

        elif escolha == '5':
            if len(animais) == 0:
                print('Nenhum animal cadastrado!')

            else:
                print('=' * 10, 'Lista de animais', '=' * 10)

                for v in animais:
                    print('Tipo:', v[0])
                    print('Brinco:', v[1])
                    print('Status:', v[2])

        elif escolha == '0':
            print('Encerrando o gerenciamento do rebanho...')
            break

        else:
            print('Opção inválida')

def login():
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
                senha = input('Digite sua senha: ')

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

                    print('=' * 10, 'Menu de Gerenciamento', '=' * 10)
                    print('[1] - Gerenciamento do Rebanho')
                    print('[2] - Gerenciamento de Produção e Derivados')
                    print('[3] - Gerenciamento do AGRO')
                    print('[0] - Sair')
                    escolha = input('Digite sua opção: ')

                    if escolha == '1':
                        rebanho()