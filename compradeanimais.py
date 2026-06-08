from cadastroanimal import animais
from listas import relatorio, comprados
from datetime import datetime
from tabulate import tabulate
from listas import produtos


def mostrar_comprovante(cliente, quantidade, total, tipo, data, hora, animais_comprados):

    print("\n" + "=" * 70)
    print("                    FAZENDA SERTÃO")
    print("                COMPROVANTE DE COMPRA")
    print("=" * 70)

    dados_compra = [
        ["Cliente", cliente],
        ["Quantidade", f"{quantidade} cabeças"],
        ["Valor Total", f"R$ {total:.2f}"],
        ["Entrega", tipo],
        ["Data", data],
        ["Hora", hora]
    ]

    print(
        tabulate(
            dados_compra,
            headers=["Informação", "Detalhe"],
            tablefmt="fancy_grid"
        )
    )

    dados_animais = []

    for animal in animais_comprados:
        dados_animais.append([
            animal["Brinco"],
            animal["Tipo"],
            f"R$ {animal['Preço']:.2f}"
        ])

    print("\nANIMAIS ADQUIRIDOS\n")

    print(
        tabulate(
            dados_animais,
            headers=["Brinco", "Tipo", "Preço"],
            tablefmt="fancy_grid"
        )
    )

    print("\nObrigado pela preferência.")
    print("=" * 70)


def compra_bovino():
    while True:

        print("\n" + "=" * 50)
        print("1 - BOI")
        print("2 - VACA")
        print("0 - SAIR")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break

        if escolha not in ["1", "2"]:
            print("Opção inválida.")
            continue

        print("\nLISTA DE ANIMAIS DISPONÍVEIS")

        quantidade_disponivel = 0

        for animal in animais:
            if animal["Status"] == "Venda":
                print(
                    f"Brinco: {animal['Brinco']} | "
                    f"Tipo: {animal['Tipo']} | "
                    f"Preço: R$ {animal['Preço']:.2f}"
                )
                quantidade_disponivel += 1

        print(f"\nQuantidade disponível: {quantidade_disponivel}")

        if quantidade_disponivel == 0:
            print("Não há animais disponíveis.")
            continue

        cliente = input("\nDigite seu nome: ")

        quantidade = int(input("Quantas cabeças deseja comprar? "))

        if quantidade > quantidade_disponivel:
            print("Quantidade indisponível.")
            continue

        total = 0
        animais_comprados = []

        vendidos = 0
        indice = 0

        while vendidos < quantidade and indice < len(animais):

            if animais[indice]["Status"] == "Venda":

                animal = animais.pop(indice)

                comprados.append(animal)
                animais_comprados.append(animal)

                total += animal["Preço"]
                vendidos += 1

            else:
                indice += 1

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

        for animal in animais_comprados:
            relatorio.append({
                "Data": data,
                "Hora": hora,
                "Ação": "Compra",
                "Cliente": cliente,
                "Brinco": animal["Brinco"],
                "Tipo": animal["Tipo"],
                "Preço": animal["Preço"],
                "Status": "Vendido",
                "Entrega": tipo,
                "Descrição": f"Animal vendido para {cliente}"
            })
        mostrar_comprovante(
            cliente,
            quantidade,
            total,
            tipo,
            data,
            hora,
            animais_comprados
        )




def compra_caprino():

        print("\nLISTA DE CAPRINOS DISPONÍVEIS")

        quantidade_disponivel = 0

        for animal in animais:
            if animal["Status"] == "Venda":
                print(
                    f"Brinco: {animal['Brinco']} | "
                    f"Tipo: {animal['Tipo']} | "
                    f"Preço: R$ {animal['Preço']:.2f}"
                )
                quantidade_disponivel += 1

        print(f"\nQuantidade disponível: {quantidade_disponivel}")

        if quantidade_disponivel == 0:
            print("Não há caprinos disponíveis.")
            return

        cliente = input("\nDigite seu nome: ")

        quantidade = int(input("Quantos caprinos deseja comprar? "))

        if quantidade > quantidade_disponivel:
            print("Quantidade indisponível.")
            return

        total = 0
        animais_comprados = []

        vendidos = 0
        indice = 0

        while vendidos < quantidade and indice < len(animais):

            if animais[indice]["Status"] == "Venda":

                animal = animais.pop(indice)

                comprados.append(animal)
                animais_comprados.append(animal)

                total += animal["Preço"]
                vendidos += 1

            else:
                indice += 1

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

        for animal in animais_comprados:

            relatorio.append({
                "Data": data,
                "Hora": hora,
                "Ação": "Compra",
                "Cliente": cliente,
                "Brinco": animal["Brinco"],
                "Tipo": animal["Tipo"],
                "Preço": animal["Preço"],
                "Status": "Vendido",
                "Entrega": tipo,
                "Descrição": f"{animal['Tipo']} vendido para {cliente}"
            })

        mostrar_comprovante(
                cliente,
                quantidade,
                total,
                tipo,
                data,
                hora,
                animais_comprados
        )

def compra_suino():

        print("\nLISTA DE SUÍNOS DISPONÍVEIS")

        quantidade_disponivel = 0

        for animal in animais:
            if animal["Status"] == "Venda":
                print(
                    f"Brinco: {animal['Brinco']} | "
                    f"Tipo: {animal['Tipo']} | "
                    f"Preço: R$ {animal['Preço']:.2f}"
                )
                quantidade_disponivel += 1

        print(f"\nQuantidade disponível: {quantidade_disponivel}")

        if quantidade_disponivel == 0:
            print("Não há suínos disponíveis.")
            return

        cliente = input("\nDigite seu nome: ")

        quantidade = int(input("Quantos suínos deseja comprar? "))

        if quantidade > quantidade_disponivel:
            print("Quantidade indisponível.")
            return

        total = 0
        animais_comprados = []

        vendidos = 0
        indice = 0

        while vendidos < quantidade and indice < len(animais):

            if animais[indice]["Status"] == "Venda":

                animal = animais.pop(indice)

                comprados.append(animal)
                animais_comprados.append(animal)

                total += animal["Preço"]
                vendidos += 1

            else:
                indice += 1

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

        for animal in animais_comprados:
            relatorio.append({
                "Data": data,
                "Hora": hora,
                "Ação": "Compra",
                "Cliente": cliente,
                "Brinco": animal["Brinco"],
                "Tipo": animal["Tipo"],
                "Preço": animal["Preço"],
                "Status": "Vendido",
                "Entrega": tipo,
                "Descrição": f"{animal['Tipo']} vendido para {cliente}"
            })

        mostrar_comprovante(
            cliente,
            quantidade,
            total,
            tipo,
            data,
            hora,
            animais_comprados
        )

def compra_leitao():

    print("\nLISTA DE LEITÕES DISPONÍVEIS")

    quantidade_disponivel = 0

    for animal in animais:
        if animal["Status"] == "Venda":
            print(
                f"Brinco: {animal['Brinco']} | "
                f"Tipo: {animal['Tipo']} | "
                f"Preço: R$ {animal['Preço']:.2f}"
            )
            quantidade_disponivel += 1

    print(f"\nQuantidade disponível: {quantidade_disponivel}")

    if quantidade_disponivel == 0:
        print("Não há leitões disponíveis.")
        return

    cliente = input("\nDigite seu nome: ")

    quantidade = int(input("Quantos leitões deseja comprar? "))

    if quantidade > quantidade_disponivel:
        print("Quantidade indisponível.")
        return

    total = 0
    animais_comprados = []

    vendidos = 0
    indice = 0

    while vendidos < quantidade and indice < len(animais):

        if animais[indice]["Status"] == "Venda":

            animal = animais.pop(indice)

            comprados.append(animal)
            animais_comprados.append(animal)

            total += animal["Preço"]
            vendidos += 1

        else:
            indice += 1

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

    for animal in animais_comprados:
        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Descrição": f"{animal['Tipo']} vendido para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados
    )



def compra_leite():

        produtos_leite = []

        for produto in produtos:
            if produto["Nome"].lower() == "leite":
                produtos_leite.append(produto)

        if not produtos_leite:
            print("Não há leite disponível.")
            return

        print("\nLISTA DE LEITES DISPONÍVEIS\n")

        tabela = []

        for i, produto in enumerate(produtos_leite, start=1):
            tabela.append([
                i,
                produto["Nome"],
                produto["Quantidade"],
                f"R$ {produto['Preço']:.2f}"
            ])

        print(
            tabulate(
                tabela,
                headers=["Nº", "Produto", "Estoque", "Preço"],
                tablefmt="fancy_grid"
            )
        )

        opcao = int(input("\nEscolha o produto: ")) - 1

        if opcao < 0 or opcao >= len(produtos_leite):
            print("Produto inválido.")
            return

        produto = produtos_leite[opcao]

        cliente = input("\nDigite seu nome: ")

        quantidade = int(input("Quantidade desejada: "))

        if quantidade > produto["Quantidade"]:
            print("Quantidade indisponível.")
            return

        total = quantidade * produto["Preço"]

        produto["Quantidade"] -= quantidade

        agora = datetime.now()

        data = agora.strftime("%d/%m/%Y")
        hora = agora.strftime("%H:%M")

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Produto",
            "Cliente": cliente,
            "Produto": produto["Nome"],
            "Quantidade": quantidade,
            "Valor Unitário": produto["Preço"],
            "Total": total,
            "Descrição": f"{quantidade} unidade(s) de {produto['Nome']} vendida(s) para {cliente}"
        })

        comprovante = [
            ["Cliente", cliente],
            ["Produto", produto["Nome"]],
            ["Quantidade", quantidade],
            ["Valor Unitário", f"R$ {produto['Preço']:.2f}"],
            ["Total", f"R$ {total:.2f}"],
            ["Data", data],
            ["Hora", hora]
        ]

        print("\nCOMPROVANTE DE COMPRA\n")

        print(
            tabulate(
                comprovante,
                headers=["Informação", "Detalhe"],
                tablefmt="fancy_grid"
            )
        )



def compra_queijo():

    queijos = []

    for produto in produtos:
        if "queijo" in produto["Nome"].lower():
            queijos.append(produto)

    if not queijos:
        print("Não há queijos disponíveis.")
        return

    print("\nLISTA DE QUEIJOS DISPONÍVEIS\n")

    tabela = []

    for i, queijo in enumerate(queijos, start=1):
        tabela.append([
            i,
            queijo["Nome"],
            queijo["Quantidade"],
            f"R$ {queijo['Preço']:.2f}"
        ])

    print(
        tabulate(
            tabela,
            headers=["Nº", "Tipo", "Estoque", "Preço"],
            tablefmt="fancy_grid"
        )
    )

    opcao = int(input("\nEscolha o queijo: ")) - 1

    if opcao < 0 or opcao >= len(queijos):
        print("Opção inválida.")
        return

    queijo = queijos[opcao]

    cliente = input("\nDigite seu nome: ")

    quantidade = int(input("Quantidade desejada: "))

    if quantidade > queijo["Quantidade"]:
        print("Quantidade indisponível.")
        return

    total = quantidade * queijo["Preço"]

    queijo["Quantidade"] -= quantidade

    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")

    relatorio.append({
        "Data": data,
        "Hora": hora,
        "Ação": "Compra Produto",
        "Cliente": cliente,
        "Produto": queijo["Nome"],
        "Quantidade": quantidade,
        "Valor Unitário": queijo["Preço"],
        "Total": total,
        "Descrição": f"{quantidade} unidade(s) de {queijo['Nome']} vendida(s) para {cliente}"
    })

    comprovante = [
        ["Cliente", cliente],
        ["Produto", queijo["Nome"]],
        ["Quantidade", quantidade],
        ["Valor Unitário", f"R$ {queijo['Preço']:.2f}"],
        ["Total", f"R$ {total:.2f}"],
        ["Data", data],
        ["Hora", hora]
    ]

    print("\nCOMPROVANTE DE COMPRA\n")

    print(
        tabulate(
            comprovante,
            headers=["Informação", "Detalhe"],
            tablefmt="fancy_grid"
        )
    )











