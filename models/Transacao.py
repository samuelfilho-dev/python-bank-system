from abc import ABC, abstractmethod, abstractproperty


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractmethod
    def registar(self, conta):
        pass
