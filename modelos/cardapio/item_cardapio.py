from abc import ABC, abstractclassmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractclassmethod # todas as classes derivadas precisam implementar
    def aplicar_desconto(self):
        pass