def total(lista, tabela):
    """Função que retorna o valor total dos produtos de uma loja dado uma lista contendo os valores dos produtos de uma loja, tal como o nome dos produtos. Entrada -> list; Saída -> float"""
    custo = 0
    for produto in lista:
        custo += dict.get(tabela, produto, 0)
    return round(custo, 2)