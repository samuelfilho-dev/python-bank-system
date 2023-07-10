from sty import fg

import mensagens
import os
import time

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(mensagens.menu))

    if opcao == 1:
        valor = float(input("Valor De Deposito: "))

        if valor < 0:
            print(mensagens.erro_valor_negativo)

        saldo += valor
        extrato += fg.cyan + f"[DEPOSITO] \t R$ {valor:.2f} \n" + fg.rs
        os.system('cls')

    elif opcao == 2:
        saque = float(input("Valor De Saque: "))

        if numeros_saques > LIMITE_SAQUES:
            print(mensagens.erro_limite_saque)
            os.system('cls')

        if saque > saldo:
            print(mensagens.erro_limite_saldo)

        if saque > limite:
            print(mensagens.erro_limite_valor_saque)
            os.system('cls')

        saldo -= saque
        numeros_saques += 1
        extrato += fg.li_red + f"[SAQUE] \t R$ {saque:.2f} \n" + fg.rs
        os.system('cls')

    elif opcao == 3:
        print("######## EXTRATO ######## \n")
        print(fg.li_red + "Não Houve realização de Movimentações \n" + fg.rs if not extrato else extrato)
        print(fg.li_blue + f"Saldo: R$ {saldo:.2f}" + fg.rs)
        time.sleep(3)
        os.system('cls')

    elif opcao == 4:
        print(mensagens.final)
        time.sleep(1)
        break

    else:
        print(mensagens.erro_opcao)
        os.system('cls')
