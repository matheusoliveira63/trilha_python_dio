menu = """

[0]Depositar 
[1]Sacar
[2]Extrato
[3]Sair

"""

saldo = 0
limite_valor_diario = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES_DIARIO=3


while True:

    opcao = input(menu)

    if opcao == "0":
        valor = float(input("Informe o valor do deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
            print("\n Valor depositado com sucesso!")
    
        else: 
            print("Operação falhou, o valor informado é inválido.")
    
    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite_valor_diario

        excedeu_saques = numero_saques >= LIMITE_SAQUES_DIARIO

        if excedeu_saldo:
            print("Saldo insuficiente.")
        
        elif excedeu_limite: 
            print("O valor do seu limite de saque é de R$500,00, contate seu gerente para aumenta-lo")
        
        elif excedeu_saques: 
            print("Você atingiu seu limite de saques diários.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Valor sacado com sucesso!")
        
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "3":
        break

    else:
        print("Opcao invalida, por favor tente umas das opcoes acima!")

