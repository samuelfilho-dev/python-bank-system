import os
import time

import funcoes
import mensagens

clientes = []
lista_cc = []

while True:
    opcao = int(input(mensagens.menu))

    if opcao == 1:
        clientes = funcoes.criar_cliente(clientes)

    elif opcao == 2:
        numero_conta = funcoes.formar_numero_da_conta(lista_cc)
        lista_cc = funcoes.criar_conta_corrente(numero_conta, clientes, lista_cc)

    elif opcao == 3:
        funcoes.listar_clientes(clientes)

    elif opcao == 4:
        funcoes.listar_conta_corrente(lista_cc)

    elif opcao == 5:
        funcoes.depositar(clientes)

    elif opcao == 6:
        funcoes.sacar(clientes)

    elif opcao == 7:
        funcoes.declarar_extrato(clientes)

    elif opcao == 8:
        print(mensagens.final)
        time.sleep(1)
        break

    else:
        print(mensagens.erro_opcao)
        os.system('cls')
