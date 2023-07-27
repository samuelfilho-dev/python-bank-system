from models.Cliente import Cliente
from sty import fg


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf

    @property
    def contas(self):
        return self._contas

    @property
    def nome(self):
        return self._nome

    def __str__(self):
        return fg.li_green + f"""
               Nome:\t{self._nome}
               Data De Nascimento:\t{self._data_nascimento}
               CPF:\t{self._cpf}
               "Enedereco":\t{self._endereco}
           """ + fg.rs
