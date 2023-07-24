from sty import fg

import os
import time
import textwrap

import mensagens


def criar_usuario(nome, data_de_nascimento, cpf, endereco, usuarios):
    """
    Esta função cria um novo usuário e adiciona-o à lista de usuários.
    Args:
        nome (str): O nome do usuário.
        data_de_nascimento (str): A data de nascimento do usuário.
        cpf (str): O CPF do usuário.
        endereco (str): O endereço do usuário.
        usuarios (list): A lista de usuários.
    Returns:
        list: A lista de usuários atualizada.
    """

    # Verifica se o CPF já existe.
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        # O CPF não existe, então exibe uma mensagem de erro.
        print(mensagens.erro_usuario_nao_encontrado)

    # Cria um novo usuário.
    usuario = {"nome": nome, "data_nascimento": data_de_nascimento, "cpf": formatar_cpf(cpf), "endereco": endereco}

    # Adiciona o usuário à lista de usuários.
    usuarios.append(usuario)

    # Exibe uma mensagem de confirmação.
    print(fg.li_green + f"O Usuário '{usuario['nome']}' Foi Cadastrado Com Sucesso" + fg.rs)

    return usuarios


def filtrar_usuario(cpf, usuarios):
    """
    Esta função filtra um usuário na lista de usuários com base no CPF.
    Args:
        cpf (str): O CPF do usuário.
        usuarios (list): A lista de usuários.
    Returns:
        dict: O usuário encontrado, ou `None` se o usuário não for encontrado.
    """

    # Cria uma lista de usuários filtrados.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    # Retorna o primeiro usuário encontrado, ou `None` se o usuário não for encontrado.
    return usuarios_filtrados[0] if usuarios_filtrados else None


def listar_usuarios(usuarios):
    """
    Esta função lista todos os usuários na lista de usuários.
    Args:
        usuarios (list): A lista de usuários.
    Returns:
        None.
    """
    # Imprime uma linha de títulos.
    print("*" * 100)
    print(fg.li_green + "Lista de Usuários" + fg.rs)
    print("*" * 100)

    # Lista cada usuário.
    for usuario in usuarios:
        linha = fg.li_green + f"""

        Nome:\t{usuario['nome']}
        Data De Nascimento:\t{usuario['data_nascimento']}
        CPF:\t{usuario['cpf']}
        Endereço:\t{usuario['endereco']}

        """ + fg.rs

        print(textwrap.dedent(linha))


def formatar_cpf(cpf):
    """Remove os caracteres de um CPF.
      Args:
        cpf (str): O CPF a ser removido.
      Returns:
        str: O CPF sem caracteres.
      """

    return cpf.replace(".", "").replace("-", "").replace("/", "")


def criar_conta_corrente(agencia, usuarios, cpf, lista_cc):
    """
    Esta função cria uma nova conta corrente para o usuário especificado.

    Args:
        agencia (int): O número da agência bancária.
        usuarios (list): A lista de usuários.
        cpf (str): O CPF do usuário.
        lista_cc (list): A lista de números de contas correntes.

    Returns:
        dict: A conta corrente criada.
    """

    # Verifica se o usuário existe.
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        # Cria um novo número de conta corrente.
        numero_conta = formar_numero_da_conta(lista_cc)

        # Cria uma nova conta corrente.
        conta_corrente = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

        # Adiciona a conta corrente à lista de contas correntes.
        lista_cc.append(conta_corrente)

        # Exibe uma mensagem de confirmação.
        print(fg.li_green + f"""
            A Conta Corrente Do Usuario '{usuario['nome']}' Foi Cadastrado Com Sucesso!

            Agencia: {agencia}
            Conta Corrente: {numero_conta}
            Usuario: {usuario}
            """ + fg.rs)

        return conta_corrente

    print(mensagens.erro_usuario_nao_encontrado)


def formar_numero_da_conta(lista_cc):
    """
    Esta função forma um novo número de conta corrente a partir da lista de números de contas correntes existentes.
    Args:
        lista_cc (list): A lista de números de contas correntes.
    Returns:
        int: O novo número de conta corrente.
    """

    # Obtém o comprimento da lista de números de contas correntes.
    length = len(lista_cc)

    # Retorna o comprimento da lista + 1.
    return length + 1


def listar_conta_corrente(lista_cc):
    """
    Esta função lista todas as contas correntes na lista de contas correntes.
    Args:
        lista_cc (list): A lista de contas correntes.
    Returns:
        None.
    """

    # Imprime uma linha de títulos.
    print("*" * 100)
    print(fg.li_green + "Lista de Contas Correntes" + fg.rs)
    print("*" * 100)

    # Lista cada conta corrente.
    for conta in lista_cc:
        linha = fg.li_green + f"""
               Agência:\t{conta['agencia']}
               C/C:\t\t{conta['numero_conta']}
               Titular:\t{conta['usuario']['nome']}
           """ + fg.rs

        print(textwrap.dedent(linha))


def sacar(*, saldo, valor, extrato, limite, numeros_saques, limite_saque):
    """
    Esta função saca dinheiro de uma conta corrente.

    Args:
        saldo (float): O saldo atual da conta corrente.
        valor (float): O valor a ser sacado.
        extrato (str): O extrato da conta corrente.
        limite (float): O limite de saques diários.
        numeros_saques (int): O número de saques realizados no dia.
        limite_saque (int): O número máximo de saques diários.

    Returns:
        float: O saldo atualizado após o saque.
        str: O extrato atualizado após o saque.
    """

    # Verifica se o número de saques realizados no dia está dentro do limite.
    if numeros_saques >= limite_saque:
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

    return saldo, extrato


def depositar(saldo, valor, extrato, /):
    """
    Esta função deposita dinheiro em uma conta corrente.

    Args:
        saldo (float): O saldo atual da conta corrente.
        valor (float): O valor a ser depositado.
        extrato (str): O extrato da conta corrente.

    Returns:
        float: O saldo atualizado com o depósito
        str: O extrato atualizado com o depósito
    """

    # Verifica se o valor a ser depositado é negativo.
    if valor < 0:
        print(mensagens.erro_valor_negativo)
        return

    # Atualiza o saldo da conta corrente.
    saldo += valor

    # Adiciona o depósito ao extrato da conta corrente.
    extrato += fg.cyan + f"[DEPOSITO] \t R$ {valor:.2f} \n" + fg.rs

    # Limpa a tela.
    os.system('cls')

    # Imprime o saldo e extrato da conta corrente.
    print(fg.li_blue + f"Saldo: R$ {saldo:.2f}" + fg.rs)
    print(fg.li_red + extrato + fg.rs)

    return saldo, extrato


def declarar_extrato(saldo, /, *, extrato):
    """
    Esta função declara o extrato de uma conta corrente.
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

    # Limpa a tela.
    os.system('cls')
