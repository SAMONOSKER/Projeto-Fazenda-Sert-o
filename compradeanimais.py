from cadastroanimal import animais
from listas import relatorio, comprados
from datetime import datetime
from tabulate import tabulate
from listas import produtos
import requests

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