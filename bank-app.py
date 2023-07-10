from sty import fg

import mensagens
import os
import time

saldo = 0
limite = 500
extrato = " ######## EXTRATO ######## \n\n"
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(mensagens.menu))

    if opcao == 1:
        valor = int(input("Valor De Deposito: "))

        if valor < 0:
            print(mensagens.erro_valor_negativo)

        saldo += valor
        extrato += fg.cyan + f"[DEPOSITO] \t R$ {valor},00 \n" + fg.rs
        os.system('cls')

    elif opcao == 2:
        saque = int(input("Valor De Saque: "))

        if numeros_saques > LIMITE_SAQUES:
            print(mensagens.erro_limite_saque)
            os.system('cls')

        if saque > saldo:
            print(mensagens.erro_limite_saldo)

        if saque > 500:
            print(mensagens.erro_limite_valor_saque)
            os.system('cls')

        saldo -= saque
        numeros_saques += 1
        extrato += fg.li_red + f"[SAQUE] \t R$ {saque},00 \n" + fg.rs
        os.system('cls')

    elif opcao == 3:
        print(extrato)
        time.sleep(3)
        os.system('cls')

    elif opcao == 4:
        break

    else:
        print(mensagens.erro_opcao)
        os.system('cls')
