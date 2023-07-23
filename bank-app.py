from sty import fg

import os
import time

import mensagens
import funcoes

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = int(input(mensagens.menu))

    if opcao == 1:
        nome = input("Nome Do Usuário: ")
        data_de_nascimento = input("Data De Nascimento (YYY-MM-DD): ")
        cpf = input("CPF: ")
        endereco = input(f"Endereço({mensagens.formato_endereco}): ")

        usuario = funcoes.criar_usuario(nome, data_de_nascimento, cpf, endereco)

        if not usuario:
            print(mensagens.erro_usuario_cadastro)

        print(f"O Usuário '{funcoes.formatar_nome_usuario(usuario[0])}' Foi Cadastrado Com Sucesso")

    elif opcao == 2:

        cpf = input("Digite Seu CPF(Sem Caracteres): ")

        if cpf not in usuario:
            print(mensagens.erro_usuario_nao_encontrado)
        else:
            nome_do_usuario = usuario[0]

            conte_corrente = funcoes.criar_conte_corrente(nome_do_usuario)

            print(f"""
                        A Conta Corrente Do Usuario '{funcoes.formatar_nome_usuario(usuario[0])}' Foi Cadastrado Com Sucesso!

                        {conte_corrente[0]}
                        {conte_corrente[1]}
                        {funcoes.formatar_nome_usuario(nome_do_usuario)}
                    """)


    elif opcao == 3:
        usuarios = funcoes.listar_usuarios()
        print(usuarios)

    elif opcao == 4:
        contas_correntes = funcoes.listar_conta_corrente()
        print(contas_correntes)

    elif opcao == 5:
        valor = float(input("Valor De Deposito: "))

        funcoes.depositar(saldo, valor, extrato)


    elif opcao == 6:
        valor = float(input("Valor Do Saque: "))

        funcoes.sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numeros_saques=numeros_saques,
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
