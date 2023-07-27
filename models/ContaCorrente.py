from sty import fg
from models.Conta import Conta
from models.Saque import Saque

import mensagens


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self._limite:
            print(mensagens.erro_limite_valor_saque)

        if numero_saques > self._limite_saques:
            print(mensagens.erro_limite_saque)

        return super().sacar(valor)

    def __str__(self):
        return fg.li_green + f"""
               Agência:\t{self.agencia}
               C/C:\t\t{self.numero}
               Titular:\t{self.cliente.nome}
           """ + fg.rs
