from cadastroanimal import animais
from  listas import relatorio
from datetime import datetime
from listas import comprados


def compra_bovino():
        while True:
            print('\n' + '=' * 50)
            print("1 - BOI")
            print("2 - VACA")
            print("0 - SAIR")

            escolha = input("Escolha uma opcao: ")

            if escolha == "1":
                print(" LISTA DE ANIMAIS DISPONIVEIS ")
                quantidade = 0
                for animal in animais:
                    if animal["Status"] == "Venda":
                     print(f"TIPO: {animal['Tipo']} | Status: {animal['Status']} | PREÇO: {animal['Preço']} ")

                     quantidade += 1

                print(f"Quantidade: {quantidade}")

                if not animais:
                    print("NAO HA BOVINOS DISPONIVEIS ")
                    return

                for i, animal in enumerate(animais, start=1):
                    print(
                        f"{i} - Brinco: {animal['Brinco']} | "
                        f"TIPO: {animal['Tipo']} | "
                        f"Status: {animal['Status']} | "
                        f"Preço: R$ {animal['Preço']:.2f}"
                    )

                    if not animais:
                        print("ESTOQUE VAZIO")
                        return

                    cliente = input("\ndigite seu nome: ")

                    quantidade = int(input("\nQuantas cabeças deseja comprar? "))

                    if quantidade > len(animais):
                        print("Quantidade indisponível.")
                        return


                    total = 0

                    for i in range(quantidade):
                        animal = animais.pop(0)  # remove do estoque
                        comprados.append(animal)
                        relatorio.append(animal)
                        total += animal["Preço"]

                    print("\n1 - Retirada")
                    print("2 - Entrega")

                    opcao = input("Escolha uma opção: ")

                    agora = datetime.now()
                    data = agora.strftime("%d/%m/%Y")
                    hora = agora.strftime("%H:%M")

                    if opcao == "1":
                        tipo = "Retirada na fazenda"
                    else:
                        tipo = "Entrega programada"



                    print("\n" + "=" * 40)
                    print("      COMPROVANTE DE COMPRA")
                    print("=" * 40)
                    print(f"Cliente: {cliente}")
                    print(f"Quantidade: {quantidade} cabeças")
                    print(f"Total: R$ {total:.2f}")
                    print(f"Agendamento: {tipo}")
                    print(f"Data: {data}")
                    print(f"Hora: {hora}")

                    print("\nAnimais adquiridos:")

                    for animal in comprados:
                        print(
                            f"Brinco: {animal['Brinco']} | "
                            f"Tipo: {animal['Tipo']} | "
                            f"Preço: R$ {animal['Preço']:.2f}"
                        )

                    print("=" * 40)









#             if escolha == "2":
#                 print(" LISTA DE ANIMAIS DISPONIVEIS ")
#                 quantidade = 0
#                 for animal in animais:
#                     if animal["Status"] == "Venda":
#                      print(f"TIPO: {animal['Tipo']}")
#                      print(f"Status: {animal['Status']}")
#                      print(f"PREÇO: {animal['Preço']}  ")
#                      quantidade += 1
#
#                 print(f"Quantidade: {quantidade}")
#
#
#
# def compra_caprino():
#     while True:








