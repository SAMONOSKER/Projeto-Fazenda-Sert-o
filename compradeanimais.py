from cadastroanimal import animais
from listas import relatorio, comprados, produtos
from datetime import datetime
from tabulate import tabulate
import requests


def clima():


        api_key = "c6be9b9a9108463743a586277abc26d1"

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q=Cajazeiras,BR"
            f"&appid={api_key}"
            f"&units=metric"
            f"&lang=pt_br"
        )

        try:
            resposta = requests.get(url, timeout=5)
            resposta.raise_for_status()

            dados = resposta.json()

            descricao = dados["weather"][0]["description"]
            temperatura = dados["main"]["temp"]

            return f"{descricao} {temperatura:.0f}°C"

        except Exception as erro:
            print("Erro da API:", erro)
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

    print("\nTIPO DE BOVINO")
    print("1 - Boi")
    print("2 - Vaca")
    print("0 - Sair")

    opcao_tipo = input("Escolha: ")

    if opcao_tipo == "0":
        return

    if opcao_tipo == "1":
        tipo_escolhido = "Bovino/Boi"

    elif opcao_tipo == "2":
        tipo_escolhido = "Bovino/Vaca"

    else:
        print("Opção inválida.")
        return

    disponiveis = []

    for animal in animais:

        if animal["Status"] != "Venda":
            continue

        if animal["Tipo"] != tipo_escolhido:
            continue

        disponiveis.append(animal)

    if len(disponiveis) == 0:
        print("Não há animais disponíveis.")
        return

    print("\nLISTA DE ANIMAIS DISPONÍVEIS")

    tabela = []

    for animal in disponiveis:
        tabela.append([
            animal["Tipo"],
            f"R$ {animal['Preço']:.2f}"
        ])

    print(
        tabulate(
            tabela,
            headers=["Tipo", "Preço"],
            tablefmt="fancy_grid"
        )
    )

    quantidade_disponivel = len(disponiveis)

    print(f"\nQuantidade disponível: {quantidade_disponivel}")

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantidade bovinos deseja comprar?: ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > quantidade_disponivel:
        print("Quantidade indisponível.")
        return

    animais_comprados = []
    total = 0

    for animal in disponiveis[:quantidade]:

        animais.remove(animal)

        comprados.append(animal)
        animais_comprados.append(animal)

        total += animal["Preço"]

    print("\n1 - Retirada")
    print("2 - Entrega")

    opcao = input("Escolha: ")

    condicao_climatica = clima()

    if opcao == "1":
        tipo = "Retirada na fazenda"

    else:

        clima_ruim = [
            "chuva",
            "rain",
            "tempestade",
            "storm",
            "garoa",
            "drizzle",
            "trovoada",
            "thunderstorm"
        ]

        if condicao_climatica.lower() == "clima indisponível":
            tipo = "Entrega programada (sem dados climáticos)"

        elif any(palavra in condicao_climatica.lower() for palavra in clima_ruim):
            tipo = "Entrega atrasada por clima ruim"

        else:
            tipo = "Entrega programada"

    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")

    for animal in animais_comprados:
        comprados.append({
            'Cliente': cliente,
            'Produto': animal['Tipo'],
            'Quantidade': quantidade,
            'Valor Unitário': animal['Preço'],
            'Valor Total': animal['Preço'],
            'Data': data,
            'Hora': hora,
            'Entrega': tipo
        })

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Bovino",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Condição climática": condicao_climatica,
            "Descrição": f"{animal['Tipo']} vendido para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados,
        condicao_climatica
    )

    print("\nCOMPRA FINALIZADA COM SUCESSO!")

def compra_caprino():

    print("\nLISTA DE CAPRINOS DISPONÍVEIS")

    caprinos_disponiveis = []

    for animal in animais:
        if animal["Status"] == "Venda" and "Caprino" in animal["Tipo"]:
            caprinos_disponiveis.append([
                animal["Brinco"],
                animal["Tipo"],
                f"R$ {animal['Preço']:.2f}"
            ])

    if not caprinos_disponiveis:
        print("Não há caprinos disponíveis.")
        return

    print(tabulate(
        caprinos_disponiveis,
        headers=["Brinco", "Tipo", "Preço"],
        tablefmt="fancy_grid"
    ))

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantos caprinos deseja comprar? : ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > len(caprinos_disponiveis):
        print("Quantidade indisponível.")
        return

    total = 0
    animais_comprados = []
    vendidos = 0
    indice = 0

    while vendidos < quantidade and indice < len(animais):

        if animais[indice]["Status"] == "Venda" and "Caprino" in animais[indice]["Tipo"]:

            animal = animais.pop(indice)

            animal["Status"] = "Vendido"

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

        clima_ruim = ["chuva", "tempestade", "garoa", "trovoada"]

        if condicao_climatica == "clima indisponível":
            tipo = "Entrega programada (sem dados climáticos)"

        elif any(p in condicao_climatica.lower() for p in clima_ruim):
            tipo = "Entrega atrasada por clima ruim"

        else:
            tipo = "Entrega programada"

    for animal in animais_comprados:

        registro = {
            'Cliente': cliente,
            'Produto': animal['Tipo'],
            'Quantidade': 1,
            'Valor Unitário': animal['Preço'],
            'Valor Total': animal['Preço'],
            'Data': data,
            'Hora': hora,
            'Entrega': tipo,
            "Brinco": animal["Brinco"]
        }

        comprados.append(registro)

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Caprino",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Condição climática": condicao_climatica,
            "Descrição": f"Caprino vendido para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados,
        condicao_climatica
    )

    return

def compra_ovino():

    print("\nLISTA DE OVELHAS DISPONÍVEIS")

    quantidade_disponivel = 0

    for animal in animais:
        if animal["Status"] == "Venda" and animal["Tipo"].lower() == "ovelha":
            print(
                f"Brinco: {animal['Brinco']} | "
                f"Tipo: {animal['Tipo']} | "
                f"Preço: R$ {animal['Preço']:.2f}"
            )
            quantidade_disponivel += 1

    if quantidade_disponivel == 0:
        print("Não há ovelhas disponíveis.")
        return

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantos ovinos deseja comprar? : ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > quantidade_disponivel:
        print("Quantidade indisponível.")
        return

    total = 0
    animais_comprados = []
    vendidos = 0
    indice = 0

    while vendidos < quantidade and indice < len(animais):

        if animais[indice]["Status"] == "Venda" and animais[indice]["Tipo"].lower() == "ovelha":

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

        clima_ruim = [
            "chuva",
            "tempestade",
            "garoa",
            "trovoada"
        ]

        if condicao_climatica == "clima indisponível":
            tipo = "Entrega programada (sem dados climáticos)"

        elif any(palavra in condicao_climatica.lower() for palavra in clima_ruim):
            tipo = "Entrega atrasada por clima ruim"

        else:
            tipo = "Entrega programada"

    for animal in animais_comprados:
        comprados.append({
            'Cliente': cliente,
            'Produto': animal['Tipo'],
            'Quantidade': quantidade,
            'Valor Unitário': animal['Preço'],
            'Valor Total': animal['Preço'],
            'Data': data,
            'Hora': hora,
            'Entrega': tipo
        })
        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Ovino",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Condição climática": condicao_climatica,
            "Descrição": f"Ovelha vendida para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados,
        condicao_climatica
    )

    return

def compra_suino():
    print("\nLISTA DE SUÍNOS DISPONÍVEIS")

    suinos_disponiveis = []

    for animal in animais:
        tipo = animal["Tipo"].lower()

        if animal["Status"] == "Venda" and "suino" in tipo:
            suinos_disponiveis.append([
                animal["Brinco"],
                animal["Tipo"],
                f"R$ {animal['Preço']:.2f}"
            ])

    if not suinos_disponiveis:
        print("Não há suínos disponíveis.")
        return

    print(tabulate(
        suinos_disponiveis,
        headers=["Brinco", "Tipo", "Preço"],
        tablefmt="fancy_grid"
    ))

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantidade: ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > len(suinos_disponiveis):
        print("Quantidade indisponível.")
        return

    total = 0
    animais_comprados = []
    vendidos = 0
    indice = 0

    while vendidos < quantidade and indice < len(animais):

        if animais[indice]["Status"] == "Venda" and "suí" in animais[indice]["Tipo"].lower():

            animal = animais.pop(indice)

            animal["Status"] = "Vendido"

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

    tipo = "Retirada na fazenda" if opcao == "1" else "Entrega programada"

    for animal in animais_comprados:

        registro = {
            "Cliente": cliente,
            "Produto": animal["Tipo"],
            "Quantidade": 1,
            "Valor Unitário": animal["Preço"],
            "Valor Total": animal["Preço"],
            "Data": data,
            "Hora": hora,
            "Entrega": tipo,
            "Brinco": animal["Brinco"]
        }

        comprados.append(registro)

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Suíno",
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
        animais_comprados,
        condicao_climatica
    )

    return


def compra_leitao():

    print("\nLISTA DE LEITÕES DISPONÍVEIS")
    leitoes_disponiveis = []

    for animal in animais:
        tipo = animal["Tipo"].lower()

        if animal["Status"] == "Venda" and "suino" in tipo:
            leitoes_disponiveis.append([
                animal["Brinco"],
                animal["Tipo"],
                f"R$ {animal['Preço']:.2f}"
            ])

    if not leitoes_disponiveis:
        print("Não há leitões disponíveis.")
        return

    print(tabulate(
        leitoes_disponiveis,
        headers=["Brinco", "Tipo", "Preço"],
        tablefmt="fancy_grid"
    ))

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantidade: ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > len(leitoes_disponiveis):
        print("Quantidade indisponível.")
        return

    total = 0
    animais_comprados = []
    vendidos = 0
    indice = 0

    while vendidos < quantidade and indice < len(animais):

        if animais[indice]["Status"] == "Venda" and "leit" in animais[indice]["Tipo"].lower():

            animal = animais.pop(indice)

            animal["Status"] = "Vendido"

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

    tipo = "Retirada na fazenda" if opcao == "1" else "Entrega programada"

    for animal in animais_comprados:

        registro = {
            "Cliente": cliente,
            "Produto": animal["Tipo"],
            "Quantidade": 1,
            "Valor Unitário": animal["Preço"],
            "Valor Total": animal["Preço"],
            "Data": data,
            "Hora": hora,
            "Entrega": tipo,
            "Brinco": animal["Brinco"]
        }

        comprados.append(registro)

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Leitão",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Descrição": f"Leitão vendido para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados,
        condicao_climatica
    )

    return

def compra_equino():

    print("\n" + "=" * 50)
    print("1 - CAVALO")
    print("2 - MULA")
    print("3 - JUMENTO")
    print("0 - SAIR")

    escolha = input("Escolha uma opção: ")

    if escolha == "0":
        return

    categoria_escolhida = None

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
            return

    elif escolha == "2":
        tipo_escolhido = "Mula"

    elif escolha == "3":
        tipo_escolhido = "Jumento"

    else:
        print("Opção inválida.")
        return

    print("\nANIMAIS DISPONÍVEIS")

    disponiveis = []
    tabela = []

    for animal in animais:

        if animal["Status"] != "Venda":
            continue

        if tipo_escolhido.lower() not in animal["Tipo"].lower():
            continue

        if categoria_escolhida:
            if categoria_escolhida.lower() not in animal["Tipo"].lower():
                continue

        disponiveis.append(animal)

        tabela.append([
            animal["Brinco"],
            animal["Tipo"],
            f"R$ {animal['Preço']:.2f}"
        ])

    quantidade_disponivel = len(disponiveis)

    if quantidade_disponivel == 0:
        print("Não há animais disponíveis.")
        return

    print(
        tabulate(
            tabela,
            headers=["Brinco", "Tipo", "Preço"],
            tablefmt="fancy_grid"
        )
    )

    print(f"\nQuantidade disponível: {quantidade_disponivel}")

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantos equinos deseja comprar? : ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > quantidade_disponivel:
        print("Quantidade indisponível.")
        return

    animais_comprados = []
    total = 0

    for animal in disponiveis[:quantidade]:

        animais.remove(animal)

        comprados.append(animal)
        animais_comprados.append(animal)

        total += animal["Preço"]

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

        clima_ruim = [
            "chuva",
            "tempestade",
            "garoa",
            "trovoada"
        ]

        if condicao_climatica == "clima indisponível":
            tipo = "Entrega programada (sem dados climáticos)"

        elif any(palavra in condicao_climatica.lower() for palavra in clima_ruim):
            tipo = "Entrega atrasada por clima ruim"

        else:
            tipo = "Entrega programada"

    for animal in animais_comprados:
        comprados.append({
            'Cliente': cliente,
            'Produto': animal['Tipo'],
            'Quantidade': quantidade,
            'Valor Unitário': animal['Preço'],
            'Valor Total': animal['Preço'],
            'Data': data,
            'Hora': hora,
            'Entrega': tipo
        })

        relatorio.append({
            "Data": data,
            "Hora": hora,
            "Ação": "Compra Equino",
            "Cliente": cliente,
            "Brinco": animal["Brinco"],
            "Tipo": animal["Tipo"],
            "Preço": animal["Preço"],
            "Status": "Vendido",
            "Entrega": tipo,
            "Condição climática": condicao_climatica,
            "Descrição": f"{animal['Tipo']} vendido para {cliente}"
        })

    mostrar_comprovante(
        cliente,
        quantidade,
        total,
        tipo,
        data,
        hora,
        animais_comprados,
        condicao_climatica
    )

    print("\nCOMPRA FINALIZADA COM SUCESSO!")

from datetime import datetime
from tabulate import tabulate

def compra_queijo():

    queijos = [
        p for p in produtos
        if "queijo" in p["Produto"].lower()
    ]

    if not queijos:
        print("Não há queijos disponíveis.")
        return

    print("\nLISTA DE QUEIJOS\n")

    for i, q in enumerate(queijos):
        print(f"{i+1} - {q['Produto']} | Estoque: {q['Quantidade']} | R$ {q['Preço']:.2f}")

    try:
        escolha = int(input("Escolha: ")) - 1
    except ValueError:
        print("Opção inválida.")
        return

    if escolha < 0 or escolha >= len(queijos):
        print("Opção inválida.")
        return

    produto = queijos[escolha]

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantidade: ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break

    if quantidade > produto["Quantidade"]:
        print("Sem estoque.")
        return

    produto["Quantidade"] -= quantidade
    total = quantidade * produto["Preço"]

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

        clima_ruim = ["chuva", "tempestade", "garoa", "trovoada"]

        if condicao_climatica == "clima indisponível":
            tipo = "Entrega programada (sem dados climáticos)"

        elif any(p in condicao_climatica.lower() for p in clima_ruim):
            tipo = "Entrega atrasada por clima ruim"

        else:
            tipo = "Entrega programada"

    relatorio.append({
        "Data": data,
        "Hora": hora,
        "Ação": "Compra Produto",
        "Cliente": cliente,
        "Produto": produto["Produto"],
        "Quantidade": quantidade,
        "Valor Unitário": produto["Preço"],
        "Status": "Vendido",
        "Entrega": tipo,
        "Condição climática": condicao_climatica,
        "Total": total,
        "Descrição": f"{quantidade} unidade(s) de {produto['Produto']} vendida(s) para {cliente}"
    })

    comprovante = [
        ["Cliente", cliente],
        ["Produto", produto["Produto"]],
        ["Quantidade", quantidade],
        ["Valor Unitário", f"R$ {produto['Preço']:.2f}"],
        ["Total", f"R$ {total:.2f}"],
        ["Data", data],
        ["Hora", hora],
        ["Entrega", tipo],
        ["Condição climática", condicao_climatica],
    ]

    print("\nCOMPROVANTE DE COMPRA\n")

    print(tabulate(
        comprovante,
        headers=["Informação", "Detalhe"],
        tablefmt="fancy_grid"
    ))

    return

def compra_leite():

    leites = [p for p in produtos if "leite" in p["Produto"].lower()]

    if not leites:
        print("Não há leite disponível.")
        return

    print("\nLISTA DE LEITES DISPONÍVEIS\n")

    tabela = []

    for i, leite in enumerate(leites, start=1):
        tabela.append([
            i,
            leite["Produto"],
            leite["Quantidade"],
            f"R$ {leite['Preço']:.2f}"
        ])

    print(
        tabulate(
            tabela,
            headers=["Nº", "Produto", "Estoque", "Preço"],
            tablefmt="fancy_grid"
        )
    )

    opcao = int(input("\nEscolha o leite: ")) - 1

    if opcao < 0 or opcao >= len(leites):
        print("Opção inválida.")
        return

    leite = leites[opcao]

    while True:

        cliente = input("\nDigite seu nome: ").strip()

        if not cliente.replace(" ", "").isalpha():
            print("Erro! Digite apenas letras.")
            continue

        quantidade = input("Quantidade: ")

        if not quantidade.isdigit():
            print("Erro! Digite apenas números.")
            continue

        quantidade = int(quantidade)

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")
            continue

        break
    if quantidade > leite["Quantidade"]:
        print("Quantidade indisponível.")
        return

    total = quantidade * leite["Preço"]

    leite["Quantidade"] -= quantidade

    agora = datetime.now()

    data = agora.strftime("%d/%m/%Y")
    hora = agora.strftime("%H:%M")

    condicao_climatica = clima()

    if opcao == "1":
        tipo = "Retirada na fazenda"
    else:
        if "chuva" in condicao_climatica.lower():
            tipo = "Entrega atrasada por clima ruim"
        else:
            tipo = "Entrega programada"

    relatorio.append({
        "Data": data,
        "Hora": hora,
        "condiçao climatica": condicao_climatica,
        "Ação": "Compra Leite",
        "Cliente": cliente,
        "Produto": leite["Produto"],
        "Quantidade": quantidade,
        "Valor Unitário": leite["Preço"],
        "Total": total,
        "Descrição": f"{quantidade} litro(s) de {leite['Produto']} vendido(s) para {cliente}"
    })

    comprovante = [
        ["Cliente", cliente],
        ["Quantidade", quantidade],
        ["Valor Total", f"R$ {total:.2f}"],
        ["Entrega", tipo],
        ["Condição climática", condicao_climatica],
        ["Data", data],
        ["Hora", hora]
    ]

    print("\nCOMPROVANTE DE COMPRA\n")

    print(tabulate(
        comprovante,
        headers=["Informação", "Detalhe"],
        tablefmt="fancy_grid"
    ))

    print("\nCOMPRA FINALIZADA COM SUCESSO!")