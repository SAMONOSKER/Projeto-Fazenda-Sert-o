import random

from menu import statusbov, statuscapri, estatusovi, estatussuino, equino, statusequino
from listas import animais




# Cadastros

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

def ovino():
    while True:
        estatusovi()
        escolha = input('Informe sua opção: ')
        if escolha == '1':
            tosquiaovi()

        elif escolha == '2':
            vendaovi()

        elif escolha == '3':
            engordaovi()

        elif escolha == '4':
            tratamentoovi()

        elif escolha == '5':
            vacinarovi()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def suino():
    while True:
        estatussuino()
        escolha = input('Informe sua opção: ')

        if escolha == '1':
            engordasui()

        elif escolha == '2':
            tratamentosui()

        elif escolha == '3':
            vacinarsui()

        elif escolha == '4':
            vendasui()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def cavalo():
    while True:
        statusequino()
        escolha = input('Informe sua opção: ')
        if escolha == '1':
            engordacavalo()

        elif escolha == '2':
            treinamentocavalo()

        elif escolha == '3':
            tratamentocavalo()

        elif escolha == '4':
            vacinarcavalo()

        elif escolha == '5':
            vendacavalo()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def mula():
      while True:
          statusequino()
          escolha = input('Informe sua opção: ')
          if escolha == '1':
              engordamula()

          elif escolha == '2':
              treinamentomula()

          elif escolha == '3':
              tratamentomula()

          elif escolha == '4':
              vacinarmula()

          elif escolha == '5':
              vendamula()

          elif escolha == '0':
              break

          else:
              print('Opção inválida!')

def jumento():
    while True:
        statusequino()
        escolha = input('Informe sua opção: ')
        if escolha == '1':
            engordajumento()

        elif escolha == '2':
            treinamentojumento()

        elif escolha == '3':
            tratamentojumento()

        elif escolha == '4':
            vacinarjumento()

        elif escolha == '5':
            vendajumento()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def equinno():
    while True:
        equino()
        escolha = input('Informe sua opção: ')

        if escolha == '1':
            cavalo()

        elif escolha == '2':
            mula()

        elif escolha == '3':
            jumento()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')






#
def linha():
    print('=' * 30)



#
#Bovino



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
                precokg = 23
                preco = peso * precokg
                animais.append({
                    'Tipo': 'Bovino/Boi',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

            print('Cadastro Concluido!')


        elif escolha == '2':
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                precokg = 23
                preco = peso * precokg
                animais.append({
                    'Tipo': 'Bovino/Vaca',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

            print('Cadastro Concluido!')


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

    print('Cadastro Cocluido!')

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

    print('Cadastro Concluido!')

#Caprino



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

    print('Cadastro Concluido!')

def vendacapri():
    linha()
    print('          ', 'Venda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(20, 50)
        precokg = 15
        preco = peso * precokg
        animais.append({
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco
        })

    print('Cadastro Concluido!')

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

    print('Cadastro Concluido!')

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

    print('Cadastro concluido!')

# Ovino





def tosquiaovi():
    linha()
    print('          ', 'Tosquia')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Tosquia'
        })

    print('Cadastro Concluido!')

def vendaovi():
    linha()
    print('          ', 'Engorda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))
    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(30, 100)
        precokg = 27
        preco = peso * precokg
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco
        })

    print('Cadastro Concluido!')


def engordaovi():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    print('Cadastro Concluido!')

def tratamentoovi():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    print('Cadastro Concluido!')

def vacinarovi():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Ovino',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    print('Cadastro Concluido!')


# Suíno/Leitão




def engordasui():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    print('Cadastro Concluido!')

def tratamentosui():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    print('Cadastro Concluido!')

def vacinarsui():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    print('Cadastro Concluido!')

def vendasui():
    linha()
    print('          ', 'Venda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(90, 150)
        precokg = 7
        preco = peso * precokg
        animais.append({
            'Tipo': 'Suíno/Leitão',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco
        })

    print('Cadastro Concluido!')


# Equinocultura




# Cavalo

def engordacavalo():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Engorda'
        })

    print('Cadastro Concluido!')

def treinamentocavalo():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

    print('Cadastro Concluido!')

def tratamentocavalo():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

    print('Cadastro Concluido!')

def vacinarcavalo():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

    print('Cadastro Concluido!')

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
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                preco = random.randint(5000, 20000)
                animais.append({
                    'Tipo': 'Equino/Cavalo',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

            print('Cadastro Concluido!')

        elif escolha == '2':

            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(250, 450)
                preco = random.randint(2000, 8000)
                animais.append({
                    'Tipo': 'Equino/Cavalo/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

            print('Cadastro Concluido!')

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')


# Mula


def engordamula():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(350, 550)
                preco = random.randint(5000, 15000)
                animais.append({
                    'Tipo': 'Equino/Mula',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preco': preco
                })

        elif escolha == '2':

            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(200, 350)
                preco = random.randint(2000, 8000)
                animais.append({
                    'Tipo': 'Equino/Mula/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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

    quantidade = int(input('Informe a quantidade de cabeças: '))

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
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(180, 350)
                preco = random.randint(3000, 10000)
                animais.append({
                    'Tipo': 'Equino/Jumento',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

        elif escolha == '2':

            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(30, 100)
                preco = random.randint(500, 2000)
                animais.append({
                    'Tipo': 'Equino/Jumento/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')


# Lista de animais


def lista():
    while True:
        linha()
        print('          ', 'Informe o Tipo')
        linha()

        print('\n[1] - Todos')
        print('[2] - Buscar o Tipo')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            for animal in animais:
                print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

        elif escolha == '2':
            while True:
                print('\n[1] - Lactação')
                print('[2] - Engorda')
                print('[3] - Venda')
                print('[4] - Tratamento')
                print('[5] - Vacinação')
                print('[0] - Sair')

                escolha = input('Informe sua opção: ')

                if escolha == '1':
                    for animal in animais:
                        if animal['Status'] == 'Lactação':
                            print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

                elif escolha == '2':
                    for animal in animais:
                        if animal['Status'] == 'Engorda':
                            print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

                elif escolha == '3':
                    for animal in animais:
                        if animal['Status'] == 'Venda':
                            print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

                elif escolha == '4':
                    for animal in animais:
                        if animal['Status'] == 'Tratamento':
                            print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

                elif escolha == '5':
                    for animal in animais:
                        if animal['Status'] == 'Vacinação':
                            print(f'Topo: {animal['Tipo']} || Peso: {animal['Peso']}kg || Brinco: {animal['Brinco']} || Status: {animal['Status']} || Preço: {animal['Preço']}')

                elif escolha == '0':
                    break

                else:
                    print('Opção inválida!')


        elif escolha == '0':
            break

        else:
            print('Opção inválida!')