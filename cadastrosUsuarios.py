from listas import usuarios

def adm():
    while True:
        nome = input('Digite seu nome de usuário: ').lower()
        if nome in usuarios:
            print('Nome de usuário existente. Informe um nome diferente!')
            continue
        senha = input('Crie sua senha: ')
        confirm = input('Confirme sua senha: ')
        if confirm != senha:
            print('Senha inválida. Confirme sua senha carretamente!')
            continue
        else:
            usuarios.append({
                'nome': nome,
                'senha': senha,
                'ID': 'ADM'
            })
            print(usuarios)
            break


def cli():
    while True:
        nome = input('Digite seu nome de usuário: ').lower()
        if nome in usuarios:
            print('Nome de usuário existente. Informe um nome diferente!')
            continue
        senha = input('Crie sua senha: ')
        confirm = input('Confirme sua senha: ')
        if confirm != senha:
            print('Senha inválida. Confirme sua senha corretamente!')
            continue
        else:
            usuarios.append({
                'nome': nome,
                'senha': senha,
                'ID': 'CLI'
            })
            print(usuarios)
            break