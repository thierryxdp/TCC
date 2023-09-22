def total(lista,valor):
    """De acordo com a lista de compra e seus valores, retorne,com 2 casas decimais, o valot total das compras"""
    i = 0
    for i in range(1,lista):
        if lista[i] in dict.items(valor):
             soma += valor
    return round(soma,2)