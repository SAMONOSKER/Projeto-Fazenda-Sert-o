from cadastrosUsuarios import adm
from cadastrosUsuarios import cli
from  login import login





print('=' * 20, 'Fazenda Sertão', '=' * 20)



while True:
    print()
    print('=' * 10, 'Menu', '=' * 10)
    print("1-Cadastro")
    print("2-Login")
    print("0-Logout")

    op = input("Digite a sua opção: ")

    if op != '1' and op != '2' and op != '0':
        print('Erro. Tente novamente.')

    elif op == "1":
        while True:
            print()
            print('=' * 10, 'CADASTRO GERAL', '=' * 10)
            print("1- Cadastar ADM")
            print("2- Cadastar CLIENTE")
            print("0- Voltar")
            escolha = input("Digite a opção: ")

            if escolha == '1':
                adm()

            elif escolha == "2":
                cli()
            elif escolha == "0":
                break

            else:
                print('Opção inválida!')

    elif op == "2":
        login()

    #                     elif escolha == '2':
    #                         print()
    #                         print('=' * 10, 'Gerenciamento de Produção e Derivados', '=' * 10)
    #
    #                         prodLeite = []
    #                         estoque = []
    #
    #                         while True:
    #                             print()
    #                             print('=' * 10, 'Produção', '=' * 10)
    #                             print('[1] - Registrar produção de leite')
    #                             print('[2] - Adicionar produto ao estoque')
    #                             print('[3] - Listar produção de leite')
    #                             print('[4] - Listar estoque')
    #                             print('[0] - Sair')
    #
    #                             escolha = input('Digite sua opção: ')
    #
    #                             if escolha == '1':
    #                                 print()
    #                                 print('=' * 5, 'Rigistrar Produção de Leite', '=' * 5)
    #
    #                                 while True:
    #                                     data = input('Data da ordenha: ')
    #
    #                                     if data > '31' or data < '00':
    #                                         print("Data inválida")
    #                                     else:
    #                                         break
    #
    #                                 litros = int(input('Litros ordenhados: '))
    #
    #                                 prod = [data, litros]
    #                                 prodLeite.append(prod)
    #
    #                                 print('Produção registrada!')
    #
    #                             elif escolha == '2':
    #                                 print()
    #                                 print('=' * 5, ' Adicionar produto ao estoque', '=' * 5)
    #
    #                                 print('[1] - Queijo Coalho')
    #                                 print('[2] - Queijo Manteiga')
    #                                 print('[0] - Sair')
    #
    #                                 escolha = input('O que deseja produzir: ')
    #
    #                                 if escolha == '1':
    #                                     print('\n', '=' * 5, 'Produzir para o Estoque', '=' * 5)
    #                                     data = input('Digite a data da ordenha: ')
    #                                     encontrado = False
    #                                     for dat in prodLeite:
    #                                         if dat[0] == data:
    #                                             encontrado = True
    #                                             prodQuejo = int(input('Quantos queijos coalho deseja produzir: '))
    #
    #                                             litros = prodQuejo * 10
    #                                             if dat[1] >= litros:
    #                                                 dat[1] -= litros
    #                                                 estoque.append([data, 'Queijo Coalho', prodQuejo, 35.00])
    #                                                 print(prodLeite)
    #                                                 print(estoque)
    #                                                 print('Queijo produzido com sucesso e adicionado ao estoque!')
    #
    #                                             else:
    #                                                 print('Leite insuficiênte.')
    #                                         else:
    #                                             print('Data da ordenha não encontrada!')
    #
    #                                 elif escolha == '2':
    #                                     print('\n', '=' * 5, 'Produzir para o Estoque', '=' * 5)
    #                                     data = input('Digite a data da ordenha: ')
    #                                     encontrado = False
    #                                     for dat in prodLeite:
    #                                         if dat[0] == data:
    #                                             encontrado = True
    #                                             print('Data encontrada!')
    #                                             prodQuejo = int(
    #                                                 input('Quantos unidades de queijo de manteiga deseja produzir: '))
    #                                             litros = prodQuejo * 15
    #                                             if dat[1] >= litros:
    #                                                 dat[1] -= litros
    #                                                 estoque.append([data, 'Queijo Mateiga', prodQuejo, 40.00])
    #                                                 print(prodLeite)
    #                                                 print(estoque)
    #                                                 print('Queijo produzido com sucesso e adicionado ao estoque!')
    #                                             else:
    #                                                 print('Leite insuficiênte.')
    #                                         else:
    #                                             print('Data da ordenha não encontrada!')
    #
    #                                 elif escolha == '0':
    #                                     print('Produção encerrada!')
    #
    #                                 else:
    #                                     print('Escolha inválida!')
    #
    #
    #
    #                             elif escolha == '3':
    #                                 print()
    #                                 print('=' * 5, 'Ver Produção de Leite', '=' * 5)
    #                                 if len(prodLeite) == 0:
    #                                     print('Nenhuma produção cadastrada!')
    #                                 else:
    #                                     print('=' * 5, 'Produção Diária de Leite', '=' * 5)
    #
    #                                     for v in prodLeite:
    #                                         print('Data:', v[0])
    #                                         print('Litros:', v[1], 'L')
    #
    #                             elif escolha == '4':
    #                                 print()
    #                                 print('=' * 5, 'Ver Estoque', '=' * 5)
    #                                 if len(estoque) == 0:
    #                                     print('Nenhum produto no estoque!')
    #
    #                                 else:
    #                                     print('=' * 5, 'Estoque de Derivados', '=' * 5)
    #
    #                                     for v in estoque:
    #                                         print('Produto:', v[1])
    #                                         print('Valor da venda: R$', v[3])
    #
    #                             elif escolha == '0':
    #                                 print('Gerenciamento de Produtos e Derivados encerrado.')
    #                                 break
    #
    #                             else:
    #                                 print('Escolha inválida!')
    #
    #                     elif escolha == '0':
    #                         print('Menu de Gerenciamento encerrado.')
    #                         break
    #
    #                     else:
    #                         print('Escolha inválida!')
    #                 break
    #
    #             logado = False
    #
    #             for cli in usuarios:
    #                 if cli[0] == usuario and cli[1] == senha:
    #                     logado = cli
    #                     print('Cliente logado com sucesso!')
    #             if logado:
    #
    #                 while True:
    #                     if logado[2] == 'CLI':
    #                         print(f"\n--- BEM VINDO A FAZENDA SERTAO SR {logado[2]} ---")
    #
    #                         print("\n--- MENU CLIENTE ---")
    #                         print("1 - Ver animais")
    #                         print("2 - Ver estoque de leite")
    #                         print("3 - Ver estoque de queijo")
    #                         print("4 - Comprar animal")
    #                         print("5 - Comprar leite")
    #                         print("6 - Comprar queijo")
    #                         print("7 - Agendamento retirada")
    #                         print("0 - Sair")
    #
    #                         op_cli = input("Escolha: ").strip()
    #
    #                         if op_cli == "1":
    #
    #                             print("\n----ANIMAIS----\n")
    #                             for animal in animais:
    #                                 print(animal)
    #
    #                         elif op_cli == "2":
    #
    #                             print("\n---ESTOQUE DE LEITE----\n")
    #                             for prod in prodLeite:
    #                                 print(f"Estoque de leite{prodLeite}", 'L')
    #
    #                         elif op_cli == "3":
    #
    #                             print("\n----ESTOQUE DE QUEIJO----\n")
    #                             for q in estoque:
    #                                 print(f'Estoque de queijo: {q}')
    #
    #                         elif op_cli == "4":
    #
    #                             print("\n----ANIMAIS----\n")
    #                             print(animais)
    #
    #                             if len(animais) == 0:
    #                                 print("Nenhum animal disponível.")
    #                             else:
    #
    #                                 Bovino = 0
    #                                 Caprino = 0
    #                                 Ovino = 0
    #                                 Suino = 0
    #                                 Leitao = 0
    #
    #                                 for animal in animais:
    #                                     tipo = animal[0].lower()
    #
    #                                     if "bovino" in tipo:
    #                                         Bovino += 1
    #                                     elif "caprino" in tipo:
    #                                         Caprino += 1
    #                                     elif "ovino" in tipo:
    #                                         Ovino += 1
    #                                     elif "suino" in tipo:
    #                                         Suino += 1
    #                                     elif "leitao" in tipo:
    #                                         Leitao += 1
    #
    #                                 print(f"Bovino: {Bovino} cabeça(s)")
    #                                 print(f"Caprino: {Caprino} cabeça(s)")
    #                                 print(f"Ovino: {Ovino} cabeça(s)")
    #                                 print(f"Suino: {Suino} cabeça(s)")
    #                                 print(f"Leitao: {Leitao} cabeça(s)")
    #
    #                                 produto = input("\nQual animal deseja comprar: ").strip().lower()
    #
    #
    #                                 animal_encontrado = None
    #
    #                                 for animal in animais:
    #                                     if animal[0].lower() == produto:
    #                                         animal_encontrado = animal
    #                                         break
    #
    #                                 if animal_encontrado:
    #                                     if "lactação" in animal_encontrado[2].lower():
    #                                         print("Animal indisponível")
    #                                     else:
    #                                         compras.append(animal_encontrado)
    #                                         animais.remove(animal_encontrado)
    #                                         print("Compra realizada")
    #                                 else:
    #                                     print("Animal não encontrado")
    #                         elif op_cli == "5":
    #
    #                             print("\n---- COMPRA DE LEITE ----\n")
    #
    #                             total_leite = 0
    #
    #                             for prod in prodLeite:
    #                                 total_leite += prod[1]
    #
    #                             if total_leite <= 0:
    #                                 print("Sem leite disponível")
    #
    #                             else:
    #                                 compra_leite = input("Quantos litros deseja comprar: ")
    #
    #                                 if compra_leite.isdigit():
    #
    #                                     compra_leite = int(compra_leite)
    #
    #                                     if compra_leite <= 0:
    #                                         print("Valor inválido")
    #
    #                                     elif compra_leite <= total_leite:
    #
    #                                         restante = compra_leite
    #
    #                                         for prod in prodLeite:
    #
    #                                             if restante > 0:
    #
    #                                                 if prod[1] >= restante:
    #                                                     prod[1] -= restante
    #                                                     restante = 0
    #
    #                                                 else:
    #                                                     restante -= prod[1]
    #                                                     prod[1] = 0
    #
    #                                         compras.append(["leite", compra_leite])
    #
    #                                         print("\nCompra realizada!")
    #                                         print(f"Você comprou {compra_leite} litros de leite")
    #                                         print(f"Leite restante: {total_leite - compra_leite} litros")
    #
    #                                     else:
    #                                         print("Estoque insuficiente de leite")
    #
    #                                 else:
    #                                     print("Digite apenas números")
    #
    #                         elif op_cli == "6":
    #
    #                             print("\n---- ESTOQUE DE QUEIJOS ----\n")
    #
    #                             for q in estoque:
    #                                 print(q)
    #
    #                             queijo = input("\nQual queijo: ").strip().lower()
    #                             qtd = int(input("Quantidade (kg): "))
    #
    #                             encontrado = False
    #
    #                             for q in estoque:
    #
    #                                 if q[1].lower() == queijo:
    #
    #                                     encontrado = True
    #
    #                                     if qtd <= q[2]:
    #
    #                                         q[2] -= qtd
    #                                         compras.append([q[1], qtd])
    #
    #                                         print("Compra realizada!")
    #                                         print(f"Você comprou {qtd}Kg de {q[1]}")
    #
    #                                         if q[2] == 0:
    #                                             estoque.remove(q)
    #
    #                                     else:
    #                                         print("Quantidade indisponível")
    #
    #                                     break
    #
    #                             if not encontrado:
    #                                 print("Queijo não encontrado")
    #
    #
    #                         elif op_cli == "7":
    #
    #                             if len(compras) == 0:
    #                                 print("Nenhuma compra")
    #                                 continue
    #
    #                             print("\n----AGENDAMENTO RETIRADA DE COMPRA----\n")
    #                             print("COMPRAS:", compras)
    #
    #                             print("\n----DIGITE OS DADOS PARA O AGENDAMENTO----\n")
    #                             produto = input("Produto: ").lower().strip()
    #
    #                             encontrado = False
    #
    #                             for c in compras:
    #                                 if c[0].lower() == produto:
    #                                     encontrado = True
    #
    #                                     compras.remove(c)
    #
    #                                     break
    #
    #                             if not encontrado:
    #                                 print("Produto não comprado")
    #                                 continue
    #
    #                             while True:
    #
    #                                 nome = input("Digite seu Nome: ").lower().strip()
    #                                 data = input("Data (dd/mm/aaaa): ")
    #                                 horario = input("Horário (hh:mm): ")
    #
    #                                 if "/" not in data or ":" not in horario:
    #                                     print("Formato inválido")
    #                                     continue
    #
    #                                 dia, mes, ano = data.split("/")
    #                                 h, m = horario.split(":")
    #
    #                                 if not (
    #                                         dia.isdigit() and mes.isdigit() and ano.isdigit() and h.isdigit() and m.isdigit()):
    #                                     print("Data ou horário inválido")
    #                                     continue
    #
    #                                 data_usuario = [int(ano), int(mes), int(dia), int(h), int(m)]
    #                                 data_atual = [2026, 5, 13, 19, 0]
    #
    #                                 if data_usuario <= data_atual:
    #                                     print("Data ou horário passado")
    #                                     continue
    #
    #                                 print("Agendamento realizado com sucesso!")
    #
    #                                 print("\n-----DADOS DO AGENDAMENTO-----\n")
    #
    #                                 print(f"comprador: {nome}")
    #                                 print(f"Produto comprado: {produto}")
    #                                 print(f"Data de retirada: {data}")
    #                                 print(f"Horário de retirada: {horario}")
    #                                 break
    #
    #
    #
    #
    #
    #                         elif op_cli == "0":
    #
    #                             print("Saindo...")
    #                             break
    #
    #                 break
    #
    # elif op == "0":
    #     print("Sistema encerrado...")
    #     break
    #
