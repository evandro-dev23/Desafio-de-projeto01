print("\n\n- - - - - - - - - - - - - - - Banco PyON® - - - - - - - - - - - - - - -")
print("                           Seja bem vindo!")
menu = ("""
    
         Serviços

- - - - - - - - - - - - - - -
    [1] - D E P Ó S I T O
    [2] - E X T R A T O
    [3] - S A Q U E
    [4] - S A I R
- - - - - - - - - - - - - - -
Digite uma opção: """)

saldo = 0
limite = 500
extrato =  ""
quantidade_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        print("Você escolheu a opção: D E P Ó S I T O\n\n")
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Valor do depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        
        else:
            print("Falha na operação!\nO valor informado é inválido.\n\n")

    elif opcao == 2:
        print("Você escolheu a opção: E X T R A T O\n\n")
        print("==================== EXTRATO BANCÁRIO ====================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n")
        print("==========================================================")

    elif opcao == 3:
        print("Você escolheu a opção: S A Q U E\n\n")
        valor = float(input("Digite o valor que deseja sacar: "))

        ultrapassou_saldo = valor > saldo
        ultrapassou_limite = valor > limite
        ultrapassou_saques = quantidade_saques >= LIMITE_SAQUES

        if ultrapassou_saldo:
            print("Falha na operação! O seu saldo é insuficiente.\n\n")
        
        elif ultrapassou_limite:
            print("Falha na operação! O valor do saque ultrapassa o limite (R$ 500,00 por saque).\n\n")
        
        elif ultrapassou_saques:
            print("Falha na operação! Você já atingiu o limite máximo de saques (3 Saques por dia).\n\n")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Valor do saque: R$ {valor:.2f}\n"
            quantidade_saques += 1
            print("Por favor, aguarde a contagem das notas...\n")
            print("Pronto!\n")
            print("Saque realizado com sucesso!")
        
        else:
            print("Falha na operação!\n O valor informado é inválido.\n\n")

    elif opcao == 4:
        print("Você escolheu a opção: S A I R\n\nSaindo...\n")
        break

    else:
        print("OPS! Opção inválida, por favor, selecione novamente a operação desejada.\n")
print("-" * 53)
print("Sua sessão foi encerrada com segurança!\nObrigado por usar os nossos serviços.\n")
print("- - - - - - - - - - - - - - - Banco PyON® - - - - - - - - - - - - - - -\n\n")