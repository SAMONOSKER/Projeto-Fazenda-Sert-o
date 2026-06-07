from listas import compras, relatorio
from cadastroanimal import animais
from menucliente import loja_animais
from compradeanimais import compra_bovino


def listar_animais():
    print('\n' + '=' * 50)
    print('        ANIMAIS DISPONÍVEIS')
    print('=' * 50)

    if len(animais) == 0:
        print("Animais nao cadastrados")

    else:
       for animal in animais:
            print(f'\nAnimal #{animal}')
            print('-' * 30)
            print(f"Tipo   : {animal[0]}")
            print(f"Brinco : {animal[1]}")
            print(f"Status : {animal[2]}")



def comprar_animais():
        loja_animais()
        escolha = input("informe sua escolha: ")
        if escolha == "1":
            compra_bovino()

        # if escolha == "2"

