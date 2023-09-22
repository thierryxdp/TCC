def num_bombons(dinheiro, preco):
    """Esta função calcula quantos bombons é possível comprar, dados o dinheiro e o preço."""
    
    dinheiro = int(input('Dinheiro: '))
    preco = int(input('Preço: '))
    bombons = dinheiro//preco
    return bombons