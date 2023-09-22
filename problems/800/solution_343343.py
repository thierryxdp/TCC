def total(lista,valor):
    """De acordo com a lista de compra e seus valores, retorne,com 2 casas decimais, o valot total das compras"""
    soma = 0
    i = 0
    for i in range(0,len(lista)):
        if lista[i] in valor.keys():
             soma = soma + valor[lista[i]] 
    return round(soma,2)