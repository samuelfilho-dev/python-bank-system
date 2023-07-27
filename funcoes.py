from models.PessoaFisica import PessoaFisica
from models.ContaCorrente import ContaCorrente
from models.Saque import Saque
from models.Deposito import Deposito
from sty import fg

import os
import textwrap
import mensagens


def verificar_cpf(clientes):
    cpf = input("Informe o CPF(Somente em números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(mensagens.erro_usuario_nao_encontrado)
        return False

    return cliente


def criar_cliente(clientes):
    cpf = input("Informe o CPF(Somente em números): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(mensagens.erro_cpf_existente)
        return

    nome = input("Nome Do Usuário: ")
    data_de_nascimento = input("Data De Nascimento(YYY-MM-DD): ")
    endereco = input(f"Endereço({mensagens.formato_endereco}): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_de_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)
    print(mensagens.sucesso_criacao_cliente)

    return clientes


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(mensagens.erro_usuario_nao_tem_conta)
        return

    return cliente.contas[0]


def listar_clientes(clientes):
    # Imprime uma linha de títulos.
    print("*" * 100)
    print(fg.li_green + "Lista de Usuários" + fg.rs)
    print("*" * 100)

    # Lista cada usuário.
    for cliente in clientes:
        print(textwrap.dedent(str(cliente)))


def criar_conta_corrente(numero_conta, clientes, lista_cc):
    cliente = verificar_cpf(clientes)

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    lista_cc.append(conta)
    cliente.contas.append(conta)

    print(mensagens.sucesso_criacao_cc)

    return lista_cc


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
        print(textwrap.dedent(str(conta)))


def sacar(clientes):
    cliente = verificar_cpf(clientes)

    valor = float(input("Informe o Valor Do Saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print(mensagens.erro_usuario_nao_tem_conta)
        return

    cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    cliente = verificar_cpf(clientes)

    valor = float(input("Qual é Valor Do Deposito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def declarar_extrato(clientes):
    extrato = ""

    cliente = verificar_cpf(clientes)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    transacoes = conta.historico.transacoes

    # Imprime o cabeçalho do extrato.
    print("######## EXTRATO ######## \n")

    # Imprime o extrato, se houver.
    if not transacoes:
        print(fg.li_red + "Não Houve realização de Movimentações \n" + fg.rs)

    else:
        for transacao in transacoes:
            extrato += (fg.li_green + f"\n{transacao['tipo']}\n\t R$ {transacao['valor']:.2f} \n\t {transacao['data']}"
                        + fg.rs)

    print(extrato)

    # Limpa a tela.
    os.system('cls')
