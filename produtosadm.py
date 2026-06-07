
from datetime import datetime
from listas import relatorio, produtos



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

        elif escolha == '0':
            break



def menucadasprod():
    print('\n[1] - Leite')
    print('[2] - Queijo')
    print('[0] - Sair')

def cadastrarproduto():
    linha()
    print('    ', 'Cadastrar Produto')
    linha()
    while True:
        menucadasprod()
        escolha = input('Informe sua opção: ')
        if escolha == '1':
            cadasleite()

        # elif escolha == '2':


        elif escolha == '0':
            break

def cadasleite():
    linha()
    print('       ','Cadastrar a Ordeinha')
    linha()

    dataordenha = input('Data da ordenha (dd/mm/aaaa): ')
    litros = float(input('Quantidade de litros: '))

    registro = {
        'Data Ordenha': dataordenha,
        'Litros': litros
    }

    produtos.append(registro)

    relatorio.append({
        'Data': datetime.now().strftime('%d/%m/%Y'),
        'Hora': datetime.now().strftime('%H:%M:%S'),
        'Ação': 'Produção de Leite',
        'Tipo': 'Leite',
        'Descrição': f'{litros} litros cadastrados',
        'Data Ordenha': dataordenha
    })

    print('Produção de leite cadastrada com sucesso!')

def queijotrad():


 def cadastrarqueijo():
    linha()
    print('      ','Cadastrar Queijo')
    linha()
#
#     while True:
#         print('\n[1] - Queijo Tradicional')
#         print('[2] - Queijo Coalho')
#         print('[3] - Queijo manteiga')
#         print('[0] - Sair')
#
#         escolha = input('Informe sua opção: ')
#
#         if escolha == '1':
