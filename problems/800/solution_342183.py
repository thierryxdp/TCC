def total(lista, tabela):
    """Função que retorna o valor total dos produtos de uma loja dado uma lista contendo os valores dos produtos de uma loja e um dicionário contendo o preço dos produtos. Entrada -> list; dict Saída -> float"""
    custo = 0
    for produto in lista:
        custo += dict.get(tabela, produto, 0)
    return round(custo, 2)