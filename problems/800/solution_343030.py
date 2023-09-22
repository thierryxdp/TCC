def total(lista,valor):
    """De acordo com a lista de compra e seus valores, retorne,com 2 casas decimais, o valot total das compras"""
    i = 0
    while valor[i]:
        i=i + 1
        lista.append(valor)
    return lista
        
        
    for i in range(1,lista):
        if lista[i] in valor:
             soma += valor
    return round(soma,2)