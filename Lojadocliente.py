from cadastroanimal import animais
from compradeanimais import compra_bovino
from compradeanimais import compra_caprino
from compradeanimais import compra_suino
from compradeanimais import compra_leitao
from compradeanimais import compra_equino
from compradeanimais import compra_queijo
from compradeanimais import compra_leite
from compradeanimais import compra_ovino
from tabulate import tabulate




def listar_animais():

    print("\nLISTA DE ANIMAIS DISPONÍVEIS")

    tabela = []

    for animal in animais:
        if animal["Status"] == "Venda":
            tabela.append([
                animal["Brinco"],
                animal["Tipo"],
                f"R$ {animal['Preço']:.2f}"
            ])

    if not tabela:
        print("Nenhum animal disponível.")
        return

    print(
        tabulate(
            tabela,
            headers=["Brinco", "Tipo", "Preço"],
            tablefmt="fancy_grid"
        )
    )



def menu_loja():
        while True:
            print("\n" + "=" * 50)
            print("        LOJA FAZENDA SERTÃO")
            print("=" * 50)

            print("1 - Comprar Bovino")
            print("2 - Comprar Caprino")
            print("3 - Comprar Ovino")
            print("4 - Comprar Suíno")
            print("5 - Comprar leitao")
            print("6 - Comprar Equino")
            print("7 - Comprar Produtos (Queijo)")
            print("8 - Comprar Produtos (leite)")
            print("0 - Sair")

            opcao = input("Digite sua opção: ")

            if opcao == "1":
                compra_bovino()

            elif opcao == "2":
                compra_caprino()

            elif opcao == "3":
                compra_ovino()

            elif opcao == "4":
                compra_suino()

            elif opcao == "5":
                compra_leitao()

            elif opcao == "6":
                compra_equino()

            elif opcao == "7":
                compra_queijo()

            elif opcao == "8":
                compra_leite()

            elif opcao == "0":
                return

