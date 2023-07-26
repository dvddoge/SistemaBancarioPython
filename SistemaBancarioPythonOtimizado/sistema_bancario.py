menu = """

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def saque(saldo, saque_valor, numero_saques, limite, extrato):
    if numero_saques == LIMITE_SAQUES:
        print("Você excedeu o limite de saques, selecione outra opção")
    elif saque_valor > limite:
        print("Esse valor é maior do que o permitido, tente novamente")
    elif saque_valor > saldo:
        print("Seu saldo é insuficiente, tente novamente")
    elif saque_valor > 0:
        saldo -= saque_valor
        extrato += f"Saque: R${saque_valor:.2f}\n"
        numero_saques += 1
        print(f"Você sacou um valor de R${saque_valor:.2f}, seu saldo atual é de R${saldo:.2f}")
    else:
        print("Operação falhou! O valor informado é inválido")

    return saldo, extrato

while True:
    
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))
        saldo += deposito
        extrato += f"Depósito: R${deposito:.2f}\n"
        print(f"Foi depositado R${deposito:.2f}, seu saldo atual é R${saldo:.2f}")
           
    elif opcao == "2":
        saque_valor = float(input("Digite o valor do saque(limitado a R$ 500,00): "))
        saque(saldo=saldo, saque_valor=saque_valor, numero_saques=numero_saques, limite=limite, extrato=extrato)
    
    elif opcao == "3":
        print("===========EXTRATO==========")
        print("Não há movimentações no seu extrato!" if not extrato else extrato)
        print(f"Saldo: R${saldo:.2f}")
        print("============================")
        
    elif opcao == "4":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")