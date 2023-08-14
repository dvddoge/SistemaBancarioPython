menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Criar Usuário
[5] - Criar Contas
[7] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
contas = []
cont = 0

def sacar(*,saldo, saque_valor, numero_saques, limite_saques, limite, extrato):
    if numero_saques > limite_saques:
        print("Você excedeu o limite de saques, selecione outra opção")
    elif saque_valor > limite:
        print("Esse valor é maior do que o permitido, tente novamente")
    elif saque_valor > saldo:
        print("Seu saldo é insuficiente, tente novamente")
    elif saque_valor > 0:
        saldo -= saque_valor
        extrato += f"Saque: R${saque_valor:.2f}\n"
        numero_saques += 1
        print(f"Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

def depositar(saldo, extrato, valor, /):
    saldo += valor
    extrato += f"Depósito: R${valor:.2f}\n"
    print(f"Depósito realizado com sucesso!")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("===========EXTRATO==========")
    print("Não há movimentações no seu extrato!" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("============================")

def validar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None
        
def criar_usuario(usuarios):
    cpf = input("Insira o seu cpf(somente números): ")
    usuario = validar_usuario(cpf, usuarios)
    if usuario:
        print("Já existe um usuário com esse cpf.")
        return None
    
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Digite sua data de nascimento(dd-mm-aaaa): ")
    endereco = input("Digite seu endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "endereco": endereco, "cpf": cpf})

    print("Usuário criado com sucesso!")

def criar_conta(cont, usuarios, contas):
    cpf = input("Informe o seu cpf")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        contas.append({usuario["nome"] : {"agencia" : "0001", "conta" : cont}})
        cont += 1
        return None

    print("Esse cpf não está cadastrado.")

while True:
    
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        saldo, extrato = depositar(saldo, extrato, deposito)
           
    elif opcao == "2":
        saque_valor = float(input("Digite o valor do saque(limitado a R$ 500,00): "))
        saldo, extrato = sacar(
            saldo=saldo, 
            saque_valor=saque_valor, 
            numero_saques=numero_saques, 
            limite_saques=LIMITE_SAQUES, 
            limite=limite, 
            extrato=extrato
        )
    
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
        
    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        criar_conta(cont, usuarios, contas)

    elif opcao == "7":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")