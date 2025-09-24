class Lanche:
    def __init__(self, nome, preco, ingredientes):
        self.nome = nome
        self.preco = preco
        self.ingredientes = ingredientes
    # Fim do construtor __init__()

    def exibirLanche(self):
        """
        Exibe as informações do lanche cadastrado. (nome, preço e ingredientes)
        """
        print(f"Sanduiche: {self.nome}; Preço: R${self.preco:.2f}; Ingredientes: {self.ingredientes}")
        # Fim do método exibirLanche

# Fim da classe Lanche





















sanduiches = [] 

for i in range(4):
  sanduiche = input("Nome do novo sanduiche:")
sanduiches.append(sanduiche)

for sanduiche in sanduiches:
    print(f"Lanche: {sanduiches}")
