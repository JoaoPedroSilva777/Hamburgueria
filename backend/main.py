from backend import cadapio
from sanduiche import Lanche

def mostrar_cardapio():
    print("\n===== CARDÁPIO DA HAMBURGUERIA =====\n")
    burgers = cadapio.listar_cardapio()
    for i, burger in enumerate(burgers, 1):
        print(f"{i}. {burger}")

def main():
    while True:
        print("=== Hamburgueria Top ===")
        print("1 - Ver Cardápio")
        print("2 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_cardapio()
        elif opcao == "2":
            print("Obrigado pela visita!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()