from sanduiche import Lanche
from cardapio import Cardapio
from bebida import Bebida
resposta = "s"
# Criação do objeto Cardápio
c = Cardapio()
while resposta == 's':
    print("Gerenciando o Cardápio")
    print("1 - Adicionar Lanche")
    print("2 - Adicionar Bebida")
    print("3 - Exibir Cardápio")
    print("4 - Sair")
    opcao = int(input("Escolha uma opção: "))

    # If da opção 1
    if opcao == 1:
        ingredientes = []
        nome = input("Nome do sanduiche: ")
        preco = float(input("Preço do sanduiche: "))
        qtdeIngredientes = int(input("Quantos ingredientes o sanduiche terá? (máximo 3): "))
        for i in range(qtdeIngredientes):
            ingrediente = input(f"Informe o ingrediente {i + 1}: ")
            ingredientes.append(ingrediente)
        # Criando o objeto Lanche dentro do laço
        l = Lanche(nome, preco, ingredientes)

        # Adicionando o lanche "l" ao cardapio "c"
        c.adicionar_item(l)

    # If da opção 2
    elif opcao == 2:
        nome = input("Nome da bebida: ")
        preco = float(input("Preço da bebida: "))
        tamanho = int(input("Tamanho da bebida (ml): "))

        # Criando o objeto Bebida dentro do laço
        b = Bebida(nome, preco, tamanho)

        # Adicionando a bebida "b" ao cardapio "c"
        c.adicionar_item(b)

    # If da opção 3
    elif opcao == 3:
        c.exibir_cardapio()

    # If da opção 4
    elif opcao == 4:
        print("Saindo do programa...")
        break
    
    resposta = input("Deseja adicionar outro item? (s/n): ")

# Fim do laço while

print(f"\nCardápio:\n{c}")
