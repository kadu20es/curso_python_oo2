from modelos.cardapio.item_cardapio import ItemCardapio


class Sobremesa(ItemCardapio):
    def __init__(self, tipo, nome, preco, tamanho, descricao):
        self._tipo = tipo
        self._nome = nome
        self._preco = preco
        self._tamanho = tamanho
        self._descricao = descricao

    @property
    def descricao(self):
        return self._descricao
    
    def aplicar_desconto(self):
        pass