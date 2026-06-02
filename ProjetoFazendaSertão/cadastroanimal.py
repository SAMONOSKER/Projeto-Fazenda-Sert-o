import random

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
    linha()
    print('          ', 'Venda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Bovino',
            'Brinco': brinco,
            'Status': 'Venda'
        })

    for animal in animais:
        print(f'Tipo: {animal['Tipo']} | Brinco: {animal['Brinco']} | Status: {animal['Status']}')

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
            'Status': 'Vacinação',
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