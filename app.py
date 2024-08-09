from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

bebida_suco = Bebida('Suco de melancia', 9.90, 'grande')
bebida_suco.aplicar_desconto()
prato_bonzinho = Prato('Paozinho de Alho', 2.00, 'O melhor pão da cidade')
prato_bonzinho.aplicar_desconto()
sobremesa = Sobremesa('Doce', 'Pudim', 12.00, '150 g', 'Deliciosa sobremesa a base de leite')
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_bonzinho)
restaurante_praca.adicionar_item_cardapio(sobremesa)


def main():
    Restaurante.listar_restaurantes()
    print(restaurante_praca.exibir_cardapio)

if __name__ == '__main__':
    main()