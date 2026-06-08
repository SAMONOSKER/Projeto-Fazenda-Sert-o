from cadastroanimal import animais
from listas import relatorio, comprados
from datetime import datetime
from tabulate import tabulate
from listas import produtos
import requests

def clima():
    try:
        url = "https://wttr.in/Cajazeiras?format=%C+%t"
        resposta = requests.get(url, timeout=5)
        condicao = resposta.text.strip().lower()

        traducoes = {
            "partly cloudy": "parcialmente nublado",
            "cloudy": "nublado",
            "clear": "céu limpo",
            "sunny": "ensolarado",
            "rain": "chuva",
            "light rain": "chuva leve",
            "heavy rain": "chuva forte"
        }

        for ingles, portugues in traducoes.items():
            if ingles in condicao:
                condicao = condicao.replace(ingles, portugues)

        return condicao

    except:
        return "clima indisponível"


def mostrar_comprovante(cliente, quantidade, total, tipo, data, hora, animais_comprados, condicao_climatica):

    print("\n" + "=" * 70)
    print("                    FAZENDA SERTÃO")
    print("                COMPROVANTE DE COMPRA")
    print("=" * 70)

    dados_compra = [
        ["Cliente", cliente],
        ["Quantidade", f"{quantidade} cabeças"],
        ["Valor Total", f"R$ {total:.2f}"],
        ["Entrega", tipo],
        ["Condição climática", condicao_climatica],
        ["Data", data],
        ["Hora", hora]
    ]

    print(tabulate(dados_compra, headers=["Informação", "Detalhe"], tablefmt="fancy_grid"))

    dados_animais = []

    for animal in animais_comprados:
        dados_animais.append([
            animal["Brinco"],
            animal["Tipo"],
            f"R$ {animal['Preço']:.2f}"
        ])

    print("\nANIMAIS ADQUIRIDOS\n")

    print(tabulate(dados_animais, headers=["Brinco", "Tipo", "Preço"], tablefmt="fancy_grid"))

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
                print(f"Brinco: {animal['Brinco']} | Tipo: {animal['Tipo']} | Preço: R$ {animal['Preço']:.2f}")
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

        condicao_climatica = clima()

        if opcao == "1":
            tipo = "Retirada na fazenda"
        else:
            if "rain" in condicao_climatica or "chuva" in condicao_climatica:
                tipo = "Entrega atrasada por clima ruim"
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
                "Condição climática": condicao_climatica,
                "Descrição": f"Animal vendido para {cliente}"
            })

        mostrar_comprovante(cliente, quantidade, total, tipo, data, hora, animais_comprados, condicao_climatica)

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


def compra_equino():

    while True:

        print("\n" + "=" * 50)
        print("1 - CAVALO")
        print("2 - MULA")
        print("3 - JUMENTO")
        print("0 - SAIR")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            break

        # ---------------- CAVALO COM CATEGORIA ----------------
        if escolha == "1":
            tipo_escolhido = "Cavalo"

            print("\n1 - Potro")
            print("2 - Adulto")

            cat = input("Escolha a categoria: ")

            if cat == "1":
                categoria_escolhida = "Potro"
            elif cat == "2":
                categoria_escolhida = "Adulto"
            else:
                print("Categoria inválida.")
                continue

        # ---------------- OUTROS ----------------
        elif escolha == "2":
            tipo_escolhido = "Mula"
            categoria_escolhida = None

        elif escolha == "3":
            tipo_escolhido = "Jumento"
            categoria_escolhida = None

        else:
            print("Opção inválida.")
            continue

        print("\nANIMAIS DISPONÍVEIS")

        quantidade_disponivel = 0

        for animal in equinos:

            if animal["Status"] != "Venda":
                continue

            if animal["Tipo"] != tipo_escolhido:
                continue

            # se for cavalo, filtra por categoria também
            if tipo_escolhido == "Cavalo":
                if animal["Categoria"] != categoria_escolhida:
                    continue

            print(
                f"Brinco: {animal['Brinco']} | "
                f"Tipo: {animal['Tipo']} | "
                f"Categoria: {animal['Categoria']} | "
                f"Preço: R$ {animal['Preço']:.2f}"
            )

            quantidade_disponivel += 1

        print(f"\nQuantidade disponível: {quantidade_disponivel}")

        if quantidade_disponivel == 0:
            print("Não há animais disponíveis.")
            continue

        cliente = input("\nDigite seu nome: ")
        quantidade = int(input("Quantos deseja comprar? "))

        if quantidade > quantidade_disponivel:
            print("Quantidade indisponível.")
            continue

        total = 0
        vendidos = 0
        animais_comprados = []
        indice = 0

        while vendidos < quantidade and indice < len(equinos):

            animal = equinos[indice]

            if animal["Status"] == "Venda" and animal["Tipo"] == tipo_escolhido:

                if tipo_escolhido == "Cavalo":
                    if animal["Categoria"] != categoria_escolhida:
                        indice += 1
                        continue

                animal = equinos.pop(indice)
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

        condicao_climatica = clima()

        if "chuva" in condicao_climatica:
            tipo = "Entrega atrasada por clima ruim"
        else:
            tipo = "Entrega programada"

        for animal in animais_comprados:
            relatorio.append({
                "Data": data,
                "Hora": hora,
                "Ação": "Compra Equino",
                "Cliente": cliente,
                "Brinco": animal["Brinco"],
                "Tipo": animal["Tipo"],
                "Categoria": animal["Categoria"],
                "Preço": animal["Preço"],
                "Status": "Vendido",
                "Entrega": tipo,
                "Condição climática": condicao_climatica,
                "Descrição": f"Equino vendido para {cliente}"
            })

        print("\nCOMPRA FINALIZADA COM SUCESSO!")

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