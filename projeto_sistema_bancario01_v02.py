import textwrap

def menu():
    menu = """
         Serviços

- - - - - - - - - - - - - - -
    [1]\tDEPÓSITO
    [2]\tEXTRATO
    [3]\tSAQUE
    [4]\tNOVA CONTA
    [5]\tNOVO USUÁRIO
    [6]\tLISTAR CONTAS
    [7]\tSAIR
- - - - - - - - - - - - - - -
Digite uma opção: """
    return int(input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Falha na operação! O valor informado é inválido. @@@")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, quantidade_saques, limite_saques):
    ultrapassou_saldo = valor > saldo
    ultrapassou_limite = valor > limite
    ultrapassou_saques = quantidade_saques >= limite_saques

    if ultrapassou_saldo:
            print("@@@ Falha na operação! O seu saldo é insuficiente. @@@\n\n")
        
    elif ultrapassou_limite:
        print("@@@ Falha na operação! O valor do saque ultrapassa o limite (R$ 500,00 por saque). @@@\n\n")
        
    elif ultrapassou_saques:
        print("@@@ Falha na operação! Você já atingiu o limite máximo de saques (3 Saques por dia). @@@\n\n")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Valor do saque:\t\tR$ {valor:.2f}\n"
        quantidade_saques += 1
        print("Por favor, aguarde a contagem das notas...\n")
        print("Pronto!\n")
        print("=== Saque realizado com sucesso! ===\n\n")
        
    else:
        print("@@@ Falha na operação!\n O valor informado é inválido. @@@\n\n")
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("==================== EXTRATO BANCÁRIO ====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo:\t\t\tR$ {saldo:.2f}\n")
    print("==========================================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Cliente criado com sucesso! ===")


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def criar_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "clientes": clientes}

    print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["clientes"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato =  ""
    quantidade_saques = 0
    clientes = []
    contas = []

    while True:
        opcao = int(menu())

        if opcao == 1:
            print("Você escolheu a opção: DEPÓSITO\n\n")
            valor = float(input("Digite o valor que deseja depositar: "))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == 2:
            print("Você escolheu a opção: EXTRATO\n\n")
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 3:
            print("Você escolheu a opção: SAQUE\n\n")
            valor = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                quantidade_saques=quantidade_saques,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif opcao == 4:
            print("Você escolheu a opção: NOVA CONTA\n\n")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        
        elif opcao == 5:
            print("Você escolheu a opção: NOVO USUÁRIO\n\n")
            criar_cliente(clientes)

        elif opcao == 6:
            print("Você escolheu a opção: LISTAR CONTAS\n\n")
            listar_contas(contas)

        elif opcao == 7:
            print("Você escolheu a opção: SAIR\n\n")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
