menu = """
Menu:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
Escolha a letra das opções:
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print('Depósito \n')
        valor_deposito = float(input("Valor do depósito: "))
        #Valor do depósito não pode ser negativo (e não faz sentido ser 0)
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
            print(f"Seu saldo atual é R$ {saldo:.2f}")
        else:
            print("Erro! O valor do depósito deve ser maior que 0")

    elif opcao == "s":
        print('Saque \n')

        #Limite de 3 saques
        if numero_saques >= LIMITE_SAQUES:
            print("Erro! Número máximo de saques excedido.")
            continue

        valor_saque = float(input("Valor do saque: "))
        #Sem saldo
        if valor_saque > saldo:
            print("Erro! Você não tem saldo suficiente.")
        #limite de 500
        elif valor_saque > 500:
            print(f"Erro! Você excedeu o limite de {limite}")
        #Valor do saque não pode ser negativo (e não faz sentido ser 0)
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques +=1
            extrato += f"Saque: R$ {valor_saque:.2f}\n"
            print(f"Seu saldo atual é R$ {saldo:.2f}")
        else:
            print("Erro! O valor do saque deve ser maior que 0.")

    elif opcao == "e":
        print('-----------------')
        print('Extrato:')
        print('-----------------')
        print(extrato)
        print('-----------------')
        print(f"Saldo Atual: R$ {saldo:.2f}")
        print('-----------------')

    elif opcao == "q":
        print("Saindo da Aplicacao")
        break

    else:
        print("Opção inválida! Tente novamente!")