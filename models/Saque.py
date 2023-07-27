from models.Transacao import Transacao


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)
