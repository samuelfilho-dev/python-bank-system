from sty import fg

import os
import time

import mensagens

lista_de_cpf = []
usuarios = []
lista_cc = []


def criar_usuario(nome, data_de_nascimento, cpf, endereco):
    """Cria um novo usuário.

    Args:
        nome (str): O nome do usuário.
        data_de_nascimento (str): A data de nascimento do usuário.
        cpf (str): O CPF do usuário.
        endereco (str): O endereço do usuário.

    Returns:
        list: Uma lista com as informações do usuário.
    """

    # Verifica se o CPF já existe.
    if cpf in lista_de_cpf:
        print(mensagens.erro_cpf_existente)
        return

    cpf = formatar_cpf(cpf)

    # Cria uma lista com as informações do usuário.
    usuario = [
        f"Nome: {nome}",
        f"Data De Nascimento: {data_de_nascimento}",
        cpf,
        f"Endereço: {endereco}",
    ]

    # Adiciona a lista de CPFs.
    lista_de_cpf.append(cpf)

    # Adiciona a lista de usuários.
    usuarios.append(usuario)

    return usuario


def listar_usuarios():
    """Lista todos os usuários.

    Returns:
        list: Uma lista com as informações de todos os usuários.
    """

    return usuarios


def formatar_cpf(cpf):
    """Remove os caracteres de um CPF.
      Args:
        cpf (str): O CPF a ser removido.
      Returns:
        str: O CPF sem caracteres.
      """

    return cpf.replace(".", "").replace("-", "").replace("/", "")


def formatar_nome_usuario(nome):
    """Formata o nome de um usuário.
    Args:
        nome (str): O nome do usuário.
    Returns:
        str: O nome do usuário formatado.
    """

    # Divide o nome em palavras.
    palavras = nome.split(" ")

    # Retorna a segunda palavra.
    return palavras[1]


def criar_conta_corrente(nome_do_usuario):
    """Cria uma nova conta corrente.

    Args:
        nome_do_usuario (str): O nome do usuário.
    Returns:
        list: Uma lista com as informações da conta corrente.
    """

    # Cria uma lista com as informações da conta corrente.
    conta_corrente = [
        "Agência: 0001",
        f"Conta Corrente: {formar_numero_da_conta()}",
        f"Usuário: {nome_do_usuario.title()}",
    ]

    lista_cc.append(conta_corrente)

    return conta_corrente


def formar_numero_da_conta():
    """Forma o número de uma conta corrente.
    Returns:
        int: O número da conta corrente.
    """

    # Inicializa o número da conta.
    numero_da_conta = 0

    # Incrementa o número da conta.
    numero_da_conta = numero_da_conta + 1

    # Retorna o número da conta.
    return numero_da_conta


def listar_conta_corrente():
    """Lista todas as contas correntes.
    Returns:
        list: Uma lista com as informações de todas as contas correntes.
    """

    return lista_cc


def sacar(saldo, valor, extrato, limite, numeros_saques, limite_saque):
    """Sacar dinheiro de uma conta corrente.

    Args:
        saldo (float): O saldo atual da conta corrente.
        valor (float): O valor a ser sacado.
        extrato (str): O extrato da conta corrente.
        limite (int): O limite de saque diário.
        numeros_saques (int): O número de saques realizados no dia.
        limite_saque (int): O limite de saques diários.

    Returns:
       bool:
       False se o saque não foi realizado
       None se o saque foi realizado com sucesso,

    """

    # Verifica se o número de saques realizados no dia está dentro do limite.
    if numeros_saques > limite_saque:
        print(mensagens.erro_limite_saque)
        os.system('cls')
        return False

    # Verifica se o valor a ser sacado é maior que o saldo.
    if valor > saldo:
        print(mensagens.erro_limite_saldo)
        os.system('cls')
        return False

    # Verifica se o valor a ser sacado é maior que o limite.
    if valor > limite:
        print(mensagens.erro_limite_valor_saque)
        os.system('cls')
        return False

    # Atualiza o saldo da conta corrente.
    saldo -= valor

    # Atualiza o número de saques realizados no dia.
    numeros_saques += 1

    # Adiciona o saque ao extrato da conta corrente.
    extrato += fg.li_red + f"[SAQUE] \t R$ {valor:.2f} \n" + fg.rs

    os.system('cls')

    # Imprime o saldo e o extrato da conta corrente.
    print(fg.li_blue + f"Saldo: R$ {saldo:.2f}" + fg.rs)
    print(fg.li_red + extrato + fg.rs)


def depositar(saldo, valor, extrato):
    """Depositar dinheiro em uma conta corrente.

    Args:
        saldo (float): O saldo atual da conta corrente.
        valor (float): O valor a ser depositado.
        extrato (str): O extrato da conta corrente.

    Returns:
        None
    """

    # Verifica se o valor a ser depositado é negativo.
    if valor < 0:
        print(mensagens.erro_valor_negativo)
        return

    # Atualiza o saldo da conta corrente.
    saldo += valor

    # Adiciona o depósito ao extrato da conta corrente.
    extrato += fg.cyan + f"[DEPOSITO] \t R$ {valor:.2f} \n" + fg.rs

    os.system('cls')

    # Imprime o saldo e extrato da conta corrente.
    print(fg.li_blue + f"Saldo: R$ {saldo:.2f}" + fg.rs)
    print(fg.li_red + extrato + fg.rs)


def declarar_extrato(saldo, *, extrato):
    """Declara o extrato de uma conta corrente.

    Args:
        saldo (float): O saldo atual da conta corrente.
        extrato (str): O extrato da conta corrente.

    Returns:
        None
    """

    # Imprime o cabeçalho do extrato.
    print("######## EXTRATO ######## \n")

    # Imprime o extrato, se houver.
    if extrato:
        print(fg.li_red + extrato + fg.rs)
    else:
        print(fg.li_red + "Não Houve realização de Movimentações \n" + fg.rs)

    # Imprime o saldo da conta corrente.
    print(fg.li_blue + f"Saldo: R$ {saldo:.2f}" + fg.rs)
    time.sleep(3)
    os.system('cls')
