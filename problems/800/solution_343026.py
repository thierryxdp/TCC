def total(lista,valor):
    """De acordo com a lista de compra e seus valores, retorne,com 2 casas decimais, o valot total das compras"""
    soma =0
    for i in range(lista):
        if lista[i] in valor:
             soma += valor
    return round(soma,2)