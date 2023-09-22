def total(lista_compras, precos):
    '''funcao qe retorna o custo total de uma compra, ao receber
    uma lista de compras de entrada e um dicionario contendo os produtos
    disponiveis com ses respectivos preços.
    list(str),dict -> float'''
    custo = 0
    for produtos in lista_compras:
        if produtos in precos:
            custo = custo + dict.get(precos,produtos)
    return custo