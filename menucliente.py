from Lojadocliente import menu_loja
from Lojadocliente import listar_animais

def menu_principal():
    while True:
        print("\n1 - Loja")
        print("2 - Listar animais")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            menu_loja()

        elif opcao == "2":
            listar_animais()

        elif opcao == "0":
            break














