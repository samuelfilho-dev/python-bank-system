from models.Historico import Historico

import mensagens


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):

        # Verifica se o valor a ser sacado é maior que o saldo.
        if valor > self.saldo:
            print(mensagens.erro_limite_saldo)
            return False

        self._saldo -= valor
        print(mensagens.sucesso_saque)
        return True

    def depositar(self, valor):

        # Verifica se o valor a ser depositado é negativo.
        if valor < 0:
            print(mensagens.erro_valor_negativo)
            return

        # Atualiza o saldo da conta corrente.
        self._saldo += valor
        print(mensagens.sucesso_deposito)
        return True
