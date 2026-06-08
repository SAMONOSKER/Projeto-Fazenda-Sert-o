
from datetime import datetime
from tabulate import tabulate
from listas import relatorio, produtos, leite, queijos



def linha():
    print('=' * 30)

def menugerenprod():
    print('\n[1] - Cadastrar Produto')
    print('[2] - Lista de produtos')
    print('[3] - Atualizar Produto')
    print('[4] - Remover Produto')
    print('[0] - Sair')

def menuprodutos():
    while True:
        linha()
        print('   ', 'Gerenciamento de Produtos')
        linha()
        menugerenprod()
        escolha = input('Informe sua opção: ')

        if escolha == '1':
            cadastrarproduto()

        elif escolha == '2':
            listarprodutos()

        elif escolha == '3':
            atualizarproduto()

        elif escolha == '4':
            removerproduto()

        elif escolha == '0':
            break

def listarprodutos():

    if not produtos:
        print('Nenhum produto cadastrado!')
        return

    dados = []

    for i, produto in enumerate(produtos, start=1):

        dados.append([
            i,
            produto.get('Produto', 'N/A'),
            produto.get('Quantidade', 0),
            f"R$ {produto.get('Preço', 0):.2f}"
        ])

    print(tabulate(
        dados,
        headers=[
            'ID',
            'Produto',
            'Quantidade',
            'Preço'
        ],
        tablefmt='fancy_grid'
    ))

def atualizarproduto():

    if not produtos:
        print('Nenhum produto cadastrado!')
        return

    listarprodutos()

    nome = input('\nInforme o nome do produto: ').strip()

    for produto in produtos:

        if produto['Produto'].lower() == nome.lower():

            print('\nProduto encontrado!')

            novaquantidade = int(input('Nova quantidade: '))

            novopreco = float(input('Novo preço: '))


            produto['Quantidade'] = novaquantidade
            produto['Preço'] = novopreco

            relatorio.append({
                'Data': datetime.now().strftime('%d/%m/%Y'),
                'Hora': datetime.now().strftime('%H:%M:%S'),
                'Ação': 'Atualização Produto',
                'Tipo': produto['Produto'],
                'Descrição':
                    f'Quantidade: {novaquantidade} | '
                    f'Preço: R$ {novopreco:.2f}'
            })

            print('Produto atualizado com sucesso!')
            return

    print('Produto não encontrado!')

def removerproduto():

    if not produtos:
        print('Nenhum produto cadastrado!')
        return

    listarprodutos()

    nome = input('\nInforme o nome do produto: ').strip()

    for produto in produtos:

        if produto['Produto'].lower() == nome.lower():

            produtos.remove(produto)

            relatorio.append({
                'Data': datetime.now().strftime('%d/%m/%Y'),
                'Hora': datetime.now().strftime('%H:%M:%S'),
                'Ação': 'Remoção Produto',
                'Tipo': produto['Produto'],
                'Descrição':
                    f"Produto removido. "
                    f"Quantidade: {produto['Quantidade']}"
            })

            print('Produto removido com sucesso!')
            return

    print('Produto não encontrado!')

def menucadasprod():
    linha()
    print('     ','Cadastro de Produtos')
    linha()
    print('\n[1] - Leite')
    print('[2] - Queijo')
    print('[0] - Sair')

def cadastrarproduto():
    while True:
        menucadasprod()
        escolha = input('Informe sua opção: ')
        if escolha == '1':
            cadasleite()

        elif escolha == '2':
            cadastrarqueijo()

        elif escolha == '0':
            break

def cadasleite():

    linha()
    print('       ', 'Cadastrar a Ordenha')
    linha()

    while True:
        try:
            litros = float(input('Quantidade de litros: ').replace(',', '.'))

            if litros <= 0:
                print('Informe uma quantidade maior que zero!')
                continue

            break

        except ValueError:
            print('Erro! Digite apenas números.')

    dataordenha = datetime.now().strftime('%d/%m/%Y')
    horaordenha = datetime.now().strftime('%H:%M:%S')

    preco_litro = 6.88
    valor_total = litros * preco_litro

    infoleite = {
        'Data Ordenha': dataordenha,
        'Hora Ordenha': horaordenha,
        'Litros': litros,
        'Preço Litro': preco_litro,
        'Valor Total': valor_total
    }

    leite.append(infoleite)

    produtos.append({
        'Produto': 'Leite',
        'Data': dataordenha,
        'Hora': horaordenha,
        'Quantidade': litros,
        'Unidade': 'Litros',
        'Preço': preco_litro,
        'Valor Total': valor_total
    })

    relatorio.append({
        'Data': dataordenha,
        'Hora': horaordenha,
        'Ação': 'Produção de Leite',
        'Tipo': 'Leite',
        'Descrição': f'{litros:.2f} litros cadastrados',
        'Valor': valor_total
    })

    print('\nProdução de leite cadastrada com sucesso!')

    dados = [
        [
            dataordenha,
            horaordenha,
            f'{litros:.2f} L',
            f'R$ {preco_litro:.2f}',
            f'R$ {valor_total:.2f}'
        ]
    ]

    print(tabulate(
        dados,
        headers=[
            'Data da Ordenha',
            'Hora',
            'Quantidade',
            'Preço/Litro',
            'Valor Total'
        ],
        tablefmt='fancy_grid'
    ))

def cadastrarqueijo():
    while True:
        linha()
        print('      ', 'Cadastrar Queijo')
        linha()
        print('\n[1] - Queijo Tradicional')
        print('[2] - Queijo Coalho')
        print('[3] - Queijo Manteiga')
        print('[0] - Sair')

        escolha = input('Informe sua opção: ')

        totalleite = sum(item['Litros'] for item in leite)

        if escolha == '1':
            linha()
            print('     ','Produzir Queijo Tradicional')
            linha()
            while True:
                try:
                    kg = float(input('Quantidade de kg produzidos: ').replace(',', '.'))

                    if kg <= 0:
                        print('Informe uma quantidade maior que zero!')
                        continue

                    break

                except ValueError:
                    print('Erro! Digite apenas números.')

            litrosnecessarios = kg * 8

            if litrosnecessarios > totalleite:
                print('Leite insuficiente!')
                print(f'Necessário: {litrosnecessarios} litros')
                print(f'Disponível: {totalleite} litros')
                continue

            leite[0]['Litros'] -= litrosnecessarios
            for produto in produtos:
                if produto['Produto'] == 'Leite':
                    produto['Quantidade'] -= litrosnecessarios
                    break

            queijo = {
                'Tipo': 'Queijo Tradicional',
                'Quantidade': kg,
                'Preço': 40,
                'Valor Total': kg * 40
            }

            queijos.append(queijo)

            produtos.append({
                'Produto': 'Queijo Tradicional',
                'Quantidade': kg,
                'Preço': 40
            })

            relatorio.append({
                'Data': datetime.now().strftime('%d/%m/%Y'),
                'Hora': datetime.now().strftime('%H:%M:%S'),
                'Ação': 'Produção de Queijo',
                'Tipo': 'Queijo Tradicional',
                'Descrição': f'{kg} kg produzidos utilizando {litrosnecessarios} litros de leite'
            })

            print('Queijo Tradicional cadastrado com sucesso!')

        elif escolha == '2':
            linha()
            print('    ','Produzir Queijo Coalho')
            linha()
            while True:
                try:
                    kg = float(input('Quantidade de kg produzidos: ').replace(',', '.'))

                    if kg <= 0:
                        print('Informe uma quantidade maior que zero!')
                        continue

                    break

                except ValueError:
                    print('Erro! Digite apenas números.')

            litrosnecessarios = kg * 10

            if litrosnecessarios > totalleite:
                print('Leite insuficiente!')
                print(f'Necessário: {litrosnecessarios} litros')
                print(f'Disponível: {totalleite} litros')
                continue

            leite[0]['Litros'] -= litrosnecessarios
            for produto in produtos:
                if produto['Produto'] == 'Leite':
                    produto['Quantidade'] -= litrosnecessarios
                    break

            queijo = {
                'Tipo': 'Queijo Coalho',
                'Quantidade': kg,
                'Preço': 45,
                'Valor Total': kg * 45
            }

            queijos.append(queijo)

            produtos.append({
                'Produto': 'Queijo Coalho',
                'Quantidade': kg,
                'Preço': 45
            })

            relatorio.append({
                'Data': datetime.now().strftime('%d/%m/%Y'),
                'Hora': datetime.now().strftime('%H:%M:%S'),
                'Ação': 'Produção de Queijo',
                'Tipo': 'Queijo Coalho',
                'Descrição': f'{kg} kg produzidos utilizando {litrosnecessarios} litros de leite'
            })

            print('Queijo Coalho cadastrado com sucesso!')

        elif escolha == '3':
            linha()
            print('    ','Produzir Queijo Manteiga')
            linha()
            while True:
                try:
                    kg = float(input('Quantidade de kg produzidos: ').replace(',', '.'))

                    if kg <= 0:
                        print('Informe uma quantidade maior que zero!')
                        continue

                    break

                except ValueError:
                    print('Erro! Digite apenas números.')

            litrosnecessarios = kg * 15

            if litrosnecessarios > totalleite:
                print('Leite insuficiente!')
                print(f'Necessário: {litrosnecessarios} litros')
                print(f'Disponível: {totalleite} litros')
                continue

            leite[0]['Litros'] -= litrosnecessarios
            for produto in produtos:
                if produto['Produto'] == 'Leite':
                    produto['Quantidade'] -= litrosnecessarios
                    break

            queijo = {
                'Tipo': 'Queijo Manteiga',
                'Quantidade': kg,
                'Preço': 55,
                'Valor Total': kg * 55
            }

            queijos.append(queijo)

            produtos.append({
                'Produto': 'Queijo Manteiga',
                'Quantidade': kg,
                'Preço': 55
            })

            relatorio.append({
                'Data': datetime.now().strftime('%d/%m/%Y'),
                'Hora': datetime.now().strftime('%H:%M:%S'),
                'Ação': 'Produção de Queijo',
                'Tipo': 'Queijo Manteiga',
                'Descrição': f'{kg} kg produzidos utilizando {litrosnecessarios} litros de leite'
            })

            print('Queijo Manteiga cadastrado com sucesso!')

        elif escolha == '0':
            break

        else:
            print('Opção inválida!')