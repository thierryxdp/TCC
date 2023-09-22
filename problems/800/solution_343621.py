def total(l,d):
    """Função que recebe uma lista de compra e um dicionário contendo o preço de cada produto
de uma loja e retorna o valor dos itens disponíveis no estoque.
list, dict -> float
teste:
total(["biscoito", "chocolate", "farinha"],{"amaciante":4.99,
"arroz":10.90,"biscoito":1.69,"cafe":6.98,"chocolate":3.79,"farinha":2.99}) == 8.47
"""
    total = 0
    for elementos in l:
        total += d[elementos]
    return round(total,2)