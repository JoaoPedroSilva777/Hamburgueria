class Bebida:
    def __init__(self, nome: str, preco: float, tamanho: int):
        self.nome = nome
        self.preco = preco
        self.tamanho = tamanho
    # Fim do construtor __init__()

    def exibirBebida(self):
        """
        Exibe as informações da bebida cadastrada. (nome, preço e tamanho)
        """
        print(f"Bebida: {self.nome}; Preço: R${self.preco:.2f}; Tamanho: {self.tamanho}ml")
    # Fim do método exibirBebida
# Fim da classe Bebida
