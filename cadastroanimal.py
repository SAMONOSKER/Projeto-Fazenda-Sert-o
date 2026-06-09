import random
from tabulate import tabulate
from menu import statusbov, statuscapri, estatusovi, estatussuino, equino, statusequino, menucadas, menutipo
from listas import animais, relatorio, comprados, leite, queijos, compras
from datetime import datetime


def relatoriogeral():
    while True:
        linha()
        print('      ','Relatório Geral')
        linha()
        print('[1] - Relatório Completo')
        print('[2] - Escolher Relatório')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            relatoriocompleto()

        elif escolha == '2':
            escolherrelatorio()

        elif escolha == '0':
            break


def relatoriocompleto():
    if not relatorio:
        print('Nenhuma movimentação registrada.')
        return

    infor = []

    for item in relatorio:
        infor.append([
            item.get('Data', 'N/A'),
            item.get('Hora', 'N/A'),
            item.get('Ação', 'N/A'),
            item.get('Brinco', 'N/A'),
            item.get('Tipo', 'N/A'),
            item.get('Status', 'N/A'),
            item.get('Descrição', 'N/A')
        ])

    print(tabulate(
        infor,
        headers=[
            'Data',
            'Hora',
            'Ação',
            'Brinco',
            'Tipo',
            'Status',
            'Descrição'
        ],
        tablefmt='fancy_grid'
    ))

def escolherrelatorio():
    while True:
        linha()
        print('       ','Escolher Relatório')
        linha()
        print('[1] - Animais')
        print('[2] - Produtos')
        print('[3] - Clientes')
        print('[0] - Sair')
        escolha = input('Informe sua opção: ')

        if escolha == '1':
            relatorioanimais()

        elif escolha == '2':
            relatorioprodutos()

        elif escolha == '3':
            relatoriocompras()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def relatorioanimais():
    if not animais:
        print('Nenhum animal cadastrado.')
        return

    infor = []

    for animal in animais:
        infor.append([
            animal.get('Brinco', 'N/A'),
            animal.get('Tipo', 'N/A'),
            animal.get('Peso', 'N/A'),
            animal.get('Status', 'N/A'),
            animal.get('Preço', 'N/A')
        ])

    print(tabulate(
        infor,
        headers=[
            'Brinco',
            'Tipo',
            'Peso (kg)',
            'Status',
            'Preço'
        ],
        tablefmt='fancy_grid'
    ))

def relatorioprodutos():
    while True:

        linha()
        print('     RELATÓRIO DE PRODUTOS')
        linha()

        print('[1] - Produção de Leite')
        print('[2] - Produção de Queijos')
        print('[0] - Voltar')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            relatorioleite()

        elif escolha == '2':
            relatorioqueijo()

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')

def relatorioleite():
    if not leite:
        print('Nenhuma produção de leite cadastrada.')
        return

    infor = []

    totallitros = 0

    for item in leite:
        totallitros += item['Litros']

        infor.append([
            item['Data Ordenha'],
            f"{item['Litros']} L",
            f"R$ {item['Preço Litro']:.2f}"
        ])

    print(tabulate(
        infor,
        headers=[
            'Data',
            'Quantidade',
            'Preço por Litro'
        ],
        tablefmt='fancy_grid'
    ))



    # def relatorioqueijo():

def relatorioqueijo():

    if not queijos:
        print('Nenhum queijo cadastrado!')
        return

    infor = []

    for item in queijos:

        infor.append([
            item.get('Tipo', 'N/A'),
            f"{item.get('Quantidade', 0)} Kg",
            f"R$ {item.get('Preço', 0):.2f}",
            f"R$ {item.get('Valor Total', 0):.2f}"
        ])

    print('\nRELATÓRIO DE QUEIJOS')

    print(tabulate(
        infor,
        headers=[
            'Tipo de Queijo',
            'Quantidade',
            'Preço/Kg',
            'Valor Total'
        ],
        tablefmt='fancy_grid'
    ))

def relatoriocompras():
    print('\nRelatório de Compras dos Clientes\n')

    if not comprados:
        print('Nenhuma compra registrada!')
        return

    infor = []
    faturamento_total = 0

    for item in comprados:
        if 'Cliente' not in item:
            continue

        faturamento_total += item.get('Valor Total', 0)

        infor.append([
            item.get('Cliente', 'N/A'),
            item.get('Produto', 'N/A'),
            item.get('Quantidade', 0),
            f"R$ {item.get('Valor Unitário', 0):.2f}",
            f"R$ {item.get('Valor Total', 0):.2f}",
            item.get('Data', 'N/A'),
            item.get('Hora', 'N/A')
        ])

    print(tabulate(
        infor,
        headers=[
            'Cliente',
            'Produto',
            'Quantidade',
            'Preço Unit.',
            'Valor Total',
            'Data',
            'Hora'
        ],
        tablefmt='fancy_grid'
    ))

    print(f'\nFATURAMENTO TOTAL: R$ {faturamento_total:.2f}')

    print('\n========== COMPROVANTES ==========\n')

    for compra in comprados:
        if 'Cliente' not in compra:
            continue
        comprovantecliente(compra)

def comprovantecliente(compra):
    infor = [[
        compra.get('Cliente', 'N/A'),
        compra.get('Produto', 'N/A'),
        compra.get('Quantidade', 0),
        f"R$ {compra.get('Valor Unitário', 0):.2f}",
        f"R$ {compra.get('Valor Total', 0):.2f}",
        compra.get('Data', 'N/A'),
        compra.get('Hora', 'N/A'),
        compra.get('Entrega', 'N/A')
    ]]

    print('\nCOMPROVANTE DE COMPRA')

    print(tabulate(
        infor,
        headers=[
            'Cliente',
            'Produto',
            'Quantidade',
            'Preço Unit.',
            'Valor Total',
            'Data',
            'Hora',
            'Entrega'
        ],
        tablefmt='fancy_grid'
    ))



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
        peso = random.randint(400, 450)
        animais.append({
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Lactação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Lactação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def engordabov():
    linha()
    print('          ', 'Engorda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(360, 420)
        animais.append({
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'
        })

    print('Cadastrado com sucesso!')

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

            linha()
            print('          ', 'Venda')
            linha()
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 450)
                precokg = 23
                preco = peso * precokg
                animais.append({
                    'Tipo': 'Bovino/Boi',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Bovino',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')


        elif escolha == '2':
            linha()
            print('          ', 'Venda')
            linha()
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 450)
                precokg = 23
                preco = peso * precokg
                animais.append({
                    'Tipo': 'Bovino/Vaca',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Bovino/Vaca',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')


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
        peso = random.randint(400, 450)
        animais.append({
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vicinabov():
    linha()
    print('          ', 'Vacinação')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(400, 450)
        animais.append({
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Bovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

#Caprino



def engordacapri():
    linha()
    print('          ', 'Engorda')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(15, 20)
        animais.append({
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

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
            'Tipo': 'Bovino/Boi',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco,
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def tratamentocapri():
    linha()
    print('          ', 'Tratamento')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(15, 20)
        animais.append({
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vacinacapri():
    linha()
    print('          ', 'Vacinação')
    linha()
    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(15, 20)
        animais.append({
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Caprino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

# Ovino





def tosquiaovi():
    linha()
    print('          ', 'Tosquia')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(40, 113)
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tosquia'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tosquia',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vendaovi():
    linha()
    print('          ', 'Venda')
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

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco,
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def engordaovi():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(28, 40)
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def tratamentoovi():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(28, 40)
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vacinarovi():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(40, 113)
        animais.append({
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Ovino',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


# Suíno/Leitão




def engordasui():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(100, 120)
        animais.append({
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def tratamentosui():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(40, 60)
        animais.append({
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vacinarsui():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(100, 120)
        animais.append({
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

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
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Suíno',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Venda',
            'Preço': preco,
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


# Equinocultura




# Cavalo

def engordacavalo():
    linha()
    print('          ', 'Engorda')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(80, 100)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def treinamentocavalo():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(450, 550)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def tratamentocavalo():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(80, 100)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

def vacinarcavalo():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(150, 250)
        animais.append({
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Cavalo',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')

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
            linha()
            print('          ', 'Venda')
            linha()
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(400, 500)
                preco = random.randint(5000, 20000)
                animais.append({
                    'Tipo': 'Equino/Cavalo/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Cavalo/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

        elif escolha == '2':

            linha()
            print('          ', 'Venda')
            linha()
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

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Cavalo/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

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
        peso = random.randint(350, 450)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def treinamentomula():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(300, 400)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def tratamentomula():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(180, 250)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def vacinarmula():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(350, 450)
        animais.append({
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Mula',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


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
            linha()
            print('          ', 'Venda')
            linha()
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(350, 550)
                preco = random.randint(5000, 15000)
                animais.append({
                    'Tipo': 'Equino/Mula/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Mula/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

        elif escolha == '2':

            linha()
            print('          ', 'Venda')
            linha()
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

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Mula/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

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
        peso = random.randint(150, 250)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Engorda',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def treinamentojumento():
    linha()
    print('          ', 'Treinamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(250, 450)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Treinamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def tratamentojumento():
    linha()
    print('          ', 'Tratamento')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(150, 250)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Tratamento',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


def vacinarjumento():
    linha()
    print('          ', 'Vacinação')
    linha()

    quantidade = int(input('Informe a quantidade de cabeças: '))

    for i in range(quantidade):
        brinco = random.randint(10000, 99999)
        peso = random.randint(250, 350)
        animais.append({
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação'
        })

        relatorio.append({
            'Data': datetime.now().strftime('%d/%m/%Y'),
            'Hora': datetime.now().strftime('%H:%M:%S'),
            'Ação': 'Cadastro',
            'Tipo': 'Equino/Jumento',
            'Peso': peso,
            'Brinco': brinco,
            'Status': 'Vacinação',
            'Descrição': 'Animal cadastrado no sistema.'

        })

    print('Cadastrado com sucesso!')


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
            linha()
            print('          ', 'Venda')
            linha()
            quantidade = int(input('Informe a quantidade de cabeças: '))

            for i in range(quantidade):
                brinco = random.randint(10000, 99999)
                peso = random.randint(180, 350)
                preco = random.randint(3000, 10000)
                animais.append({
                    'Tipo': 'Equino/Jumento/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco
                })

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Jumento/Adulto',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

        elif escolha == '2':

            linha()
            print('          ', 'Venda')
            linha()
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

                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Cadastro',
                    'Tipo': 'Equino/Jumento/Potro',
                    'Peso': peso,
                    'Brinco': brinco,
                    'Status': 'Venda',
                    'Preço': preco,
                    'Descrição': 'Animal cadastrado no sistema.'

                })

            print('Cadastrado com sucesso!')

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')


# Lista de animais


def lista():
    while True:
        linha()
        print('          ','Informe o Tipo')
        linha()

        print('\n[1] - Todos')
        print('[2] - Buscar o Tipo')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        if escolha == '1':
            info = []
            for animal in animais:
                info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg', animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'), f'R$ {animal.get('Preço', 0):,.2f}'])
            print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

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
                    info = []
                    for animal in animais:
                        if animal['Status'] == 'Lactação':
                            info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg',animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'),f'R$ {animal.get('Preço', 0):,.2f}'])
                    print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

                elif escolha == '2':
                    info = []
                    for animal in animais:
                        if animal['Status'] == 'Engorda':
                            info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg',animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'),f'R$ {animal.get('Preço', 0):,.2f}'])
                    print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

                elif escolha == '3':
                    info = []
                    for animal in animais:
                        if animal['Status'] == 'Venda':
                            info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg',animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'),f'R$ {animal.get('Preço', 0):,.2f}'])
                    print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

                elif escolha == '4':
                    info = []
                    for animal in animais:
                        if animal['Status'] == 'Tratamento':
                            info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg',animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'),f'R$ {animal.get('Preço', 0):,.2f}'])
                    print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

                elif escolha == '5':
                    info = []
                    for animal in animais:
                        if animal['Status'] == 'Vacinação':
                            info.append([animal.get('Tipo', 'N/A'), f'{animal.get('Peso', 'Não informado')} kg',animal.get('Brinco', 'N/A'), animal.get('Status', 'N/A'),f'R$ {animal.get('Preço', 0):,.2f}'])
                    print(tabulate(info, headers=['Tipo', 'Peso', 'Brinco', 'Status', 'Preço'], tablefmt='fancy_grid'))

                elif escolha == '0':
                    break

                else:
                    print('Opção inválida!')


        elif escolha == '0':
            break

        else:
            print('Opção inválida!')




def atualizaranimal():
        linha()
        print('          ','Atualizar Animal')
        linha()

        brinco = int(input('Informe o brinco do animal: '))

        for animal in animais:

            if animal['Brinco'] == brinco:

                print('\n1 - Peso')
                print('2 - Status')
                print('3 - Preço')

                opcao = input('O que deseja atualizar? ')

                if opcao == '1':

                    pesoantigo = animal.get('Peso', 'Não informado')

                    novo = float(input('Novo peso: '))
                    animal['Peso'] = novo

                    relatorio.append({
                        'Data': datetime.now().strftime('%d/%m/%Y'),
                        'Hora': datetime.now().strftime('%H:%M:%S'),
                        'Ação': 'Atualização',
                        'Brinco': animal.get('Brinco', 'N/A'),
                        'Tipo': animal.get('Tipo', 'N/A'),
                        'Status': animal.get('Status', 'N/A'),
                        'Descrição': f'Peso alterado de {pesoantigo} kg para {novo} kg'
                    })

                    print('Peso atualizado com sucesso!')

                elif opcao == '2':

                    statusantigo = animal['Status']

                    novo = input('Novo status: ')
                    animal['Status'] = novo

                    relatorio.append({
                        'Data': datetime.now().strftime('%d/%m/%Y'),
                        'Hora': datetime.now().strftime('%H:%M:%S'),
                        'Ação': 'Atualização',
                        'Brinco': animal.get('Brinco', 'N/A'),
                        'Tipo': animal.get('Tipo', 'N/A'),
                        'Status': animal.get('Status', 'N/A'),
                        'Descrição': f'Status alterado de {statusantigo} para {novo}'
                    })

                    print('Status atualizado com sucesso!')

                elif opcao == '3':

                    precoantigo = animal.get('Preço', 0)

                    novo = float(input('Novo preço: '))
                    animal['Preço'] = novo

                    relatorio.append({
                        'Data': datetime.now().strftime('%d/%m/%Y'),
                        'Hora': datetime.now().strftime('%H:%M:%S'),
                        'Ação': 'Atualização',
                        'Brinco': animal.get('Brinco', 'N/A'),
                        'Tipo': animal.get('Tipo', 'N/A'),
                        'Status': animal.get('Status', 'N/A'),
                        'Descrição': (f'Preço alterado de R$ {precoantigo:,.2f} para R$ {novo:,.2f}')
                    })

                    print('Preço atualizado com sucesso!')

                return

        print('Animal não encontrado!')


def removeranimal():
    linha()
    print('       ','Remover Animal')
    linha()

    brinco = int(input('Digite o número do brinco: '))

    for animal in animais:

        if animal['Brinco'] == brinco:

            print('\nAnimal encontrado:')
            print(f"Brinco: {animal['Brinco']}")
            print(f"Tipo: {animal['Tipo']}")
            print(f"Status: {animal['Status']}")

            print('\nTem certeza que deseja remover o animal?')
            print('[1] - Sim')
            print('[2] - Não')
            escolha = input('Informe sua opção: ')

            if escolha == '1':
                animais.remove(animal)
                relatorio.append({
                    'Data': datetime.now().strftime('%d/%m/%Y'),
                    'Hora': datetime.now().strftime('%H:%M:%S'),
                    'Ação': 'Remoção',
                    'Brinco': animal.get('Brinco', 'N/A'),
                    'Tipo': animal.get('Tipo', 'N/A'),
                    'Status': animal.get('Status', 'N/A'),
                    'Descrição': 'Animal removido do sistema'
                })
                print('Animal removido com sucesso!')
            elif escolha == '2':
                print('Operação cancelada.')

            return

    print('Animal não encontrado!')





