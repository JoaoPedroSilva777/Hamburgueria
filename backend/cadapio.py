from sanduiche import Sanduiche

# Lista do cardápio
_cardapio = [
    Sanduiche(
        nome="Cheddar Bacon",
        preco=25.90,
        descricao="Pão brioche, hambúrguer 180g, cheddar derretido, bacon crocante.",
        imagem="/static/img/cheddar_bacon.jpg"
    ),
    Sanduiche(
        nome="Classic Burger",
        preco=22.00,
        descricao="Pão tradicional, hambúrguer 150g, queijo prato, alface e tomate.",
        imagem="/static/img/classic_burger.jpg"
    ),
    Sanduiche(
        nome="Veggie Delight",
        preco=21.50,
        descricao="Hambúrguer vegetariano, rúcula, tomate seco e maionese verde.",
        imagem="/static/img/veggie.jpg"
    ),
    Sanduiche(
        nome="Duplo Smash",
        preco=29.90,
        descricao="Dois smash burgers de 100g, queijo, picles e molho especial.",
        imagem="/static/img/duplo_smash.jpg"
    )
]

def listar_cardapio():
    return _cardapio

def buscar_por_nome(nome):
    return next((s for s in _cardapio if s.nome.lower() == nome.lower()), None)

def adicionar_sanduiche(sanduiche):
    if isinstance(sanduiche, Sanduiche):
        _cardapio.append(sanduiche)
        return True
    return False

def remover_por_nome(nome):
    global _cardapio
    _cardapio = [s for s in _cardapio if s.nome.lower() != nome.lower()]
