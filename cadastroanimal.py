import random

from main import escolha

animais = []


def linha():
    print('=' * 30)

def menucadas():
    print()
    print('=' * 10, 'Cadastrar animal', '=' * 10)
    print('[1] - Bovino')
    print('[2] - Caprino')
    print('[3] - Ovino')
    print('[4] - Suíno/Leitão')
    print('[5] - Equinocultura')


#Bovino

def statusbov():
    print('[1] - Lactação')
    print('[2] - Engorda')
    print('[3] - Venda')
    print('[4] - Tratamento')
    print('[5] - Vacinação')
    print('[0] - Sair')

def lactabov():
    linha()
    print('          ', 'Lactação')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Bovino',
            'Brinco': brinco,
            'Status': 'Lactação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def engordabov():
    linha()
    print('          ', 'Engorda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Bovino',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def vendabov():
    while True:
        linha()
        print('          ', 'Venda')
        linha()
        print('\n[1] - Boi/Garrote')
        print('[2] - Vaca')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':

            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(450, 600)
                animais.append({
                    'Tipo': 'Bovino',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

            for animal in animais:
                print(f'Tipo: {animal['Tipo']} | Peso: {animal['peso']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


        elif escolha == '2':
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)

                animais.append({
                    'Tipo': 'Bovino',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

            for animal in animais:
                print(f'Tipo: {animal['Tipo']} | Peso: {animal['peso']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def tratamentobov():
    linha()
    print('          ', 'Tratamento')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Bovino',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def vicinabov():
    linha()
    print('          ', 'Vacinação')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Bovino',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


#Caprino

def statuscapri():
    print('\n[1] - Engorda')
    print('[2] - Venda')
    print('[3] - Tratamento')
    print('[4] - Vacinação')
    print('[0] - Sair')

def engordacapri():
    linha()
    print('          ', 'Engorda')
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Caprino',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def vendacapri():
    linha()
    print('          ', 'Venda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Caprino',
            'Brinco': brinco,
            'Status': 'Venda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def tratamentocapri():
    linha()
    print('          ', 'Tratamento')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Caprino',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

def vacinacapri():
    linha()
    print('          ', 'Vacinação')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Caprino',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


# Ovino


def estatusovi():
    print('\n[1] - Tosquia')
    print('[2] - Venda')
    print('[3] - Engorda')
    print('[4] - Tratamento')
    print('[5] - Vacinação')
    print('[0] - Sair')


def tosquiaovi():
    linha()
    print('          ', 'Tosquia')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Tosquia'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vendaovi():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(30, 50)
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Peso: {animal['Peso']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def engordaovi():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def tratamentoovi():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vacinarovi():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')



# Suíno/Leitão


def estatussuino():
    print('\n[1] - Engorda')
    print('[2] - Tratamento')
    print('[3] - Vacinação')
    print('[4] - Venda')
    print('[0] - Sair')


def engordasui():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def tratamentosui():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vacinarsui():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vendasui():
    linha()
    print('          ', 'Venda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(90, 150)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')



# Equinocultura


def equino():
    while True:
        print('\n[1] - Cavalo')
        print('[2] - Mula')
        print('[3] - Jumentos')
        print('[0] - Sair')


def statusequino():
    print('\n[1] - Engorda')
    print('[2] - Treinamento')
    print('[3] - Tratamento')
    print('[4] - Vacinação')
    print('[5] - Venda')
    print('[0] - Sair')



# Cavalo

def engordacavalo():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def treinamentocavalo():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def tratamentocavalo():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vacinarcavalo():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vendacavalo():
    linha()
    print('          ', 'Venda')
    linha()
    while True:
        print('\n[1] - Adulto')
        print('[2] - Potro')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                animais.append({
                    'Tipo': 'Equino/Cavalo',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '2':

            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(300, 350)
                animais.append({
                    'Tipo': 'Equino/Cavalo/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')


# Mula


def engordamula():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/mula',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def treinamentomula():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def tratamentomula():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vacinarmula():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vendamula():
    linha()
    print('          ', 'Venda')
    linha()
    while True:
        print('\n[1] - Adulto')
        print('[2] - Potro')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                animais.append({
                    'Tipo': 'Equino/Mula',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '2':

            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(300, 350)
                animais.append({
                    'Tipo': 'Equino/Mula/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')


# Jumento


def engordajumento():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def treinamentojumento():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def tratamentojumento():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vacinarjumento():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = input('Informe a quantidade de cabeças: ')

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')


def vendajumento():
    linha()
    print('          ', 'Venda')
    linha()
    while True:
        print('\n[1] - Adulto')
        print('[2] - Potro')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                animais.append({
                    'Tipo': 'Equino/Jumento',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '2':

            quantidade = input('Informe a quantidade de cabeças: ')

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(300, 350)
                animais.append({
                    'Tipo': 'Equino/Jumento/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda'
                })

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

