from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8)
restaurante_praca.receber_avaliacao('Emy', 2)

bebida_suco = Bebida('Suco de melancia', 9.90, 'grande')
prato_bonzinho = Prato('Paozinho de Alho', 2.00, 'O melhor pão da cidade')
restaurante_praca.adicionar_item_cardapio(bebida_suco)
restaurante_praca.adicionar_item_cardapio(prato_bonzinho)

def main():
    Restaurante.listar_restaurantes()
    print(restaurante_praca.exibir_cardapio)

if __name__ == '__main__':
    main()