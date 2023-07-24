import os
import time

import mensagens
import funcoes

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3
usuarios = []
lista_cc = []

while True:
    opcao = int(input(mensagens.menu))

    if opcao == 1:
        nome = input("Nome Do Usuário: ")
        data_de_nascimento = input("Data De Nascimento (YYY-MM-DD): ")
        cpf = input("CPF: ")
        endereco = input(f"Endereço({mensagens.formato_endereco}): ")

        usuarios = funcoes.criar_usuario(nome, data_de_nascimento, cpf, endereco, usuarios)

    elif opcao == 2:

        cpf = input("Digite Seu CPF(Sem Caracteres): ")
        AGENCIA = "0001"
        conta_corrente = funcoes.criar_conta_corrente(AGENCIA, usuarios, cpf, lista_cc)
        # lista_cc.append(conta_corrente)

    elif opcao == 3:
        funcoes.listar_usuarios(usuarios)

    elif opcao == 4:
        funcoes.listar_conta_corrente(lista_cc)

    elif opcao == 5:
        valor = float(input("Valor De Deposito: "))

        saldo, extrato = funcoes.depositar(saldo, valor, extrato)

    elif opcao == 6:
        valor = float(input("Valor Do Saque: "))

        saldo, extrato = funcoes.sacar(saldo=saldo,
                                       valor=valor,
                                       extrato=extrato,
                                       limite=limite,
                                       numeros_saques=numeros_saques,
                                       limite_saque=LIMITE_SAQUES)

    elif opcao == 7:
        funcoes.declarar_extrato(saldo, extrato=extrato)

    elif opcao == 8:
        print(mensagens.final)
        time.sleep(1)
        break

    else:
        print(mensagens.erro_opcao)
        os.system('cls')
