from sanduiche import Lanche
from bebida import Bebida
class Cardapio:
    def __init__(self):
        self.itens = []
        self.categoria = ""

    # Criação do método adicionarItem()
    def adicionarItem(self,item, categoria):
        """
        Adiciona um item ao cardápio.
        """
        self.itens.append(item)
        self.categoria = categoria
    # Fim do método adicionarItem() 

    # Criação do método exibirCardapio()
    def exibirCardapio(self):
        """
        Exibe o cardápio completo com todos os lanches e bebidas cadastrados.
        """
        for item in self.itens:
            if item.categoria == "Bebida":
                item.exibirBebida()
            else:
                item.exibirLanche()
        # Fim do método exibirCardapio()

# Fim da classe