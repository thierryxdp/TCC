def total(lista,dicio):
    """
    recebe uma lista de compras e um dicionário com o preço dos
    produtos e retorna o valor total dos itens na lista.
    """
    
    total=0
    
    for x in lista:
        total=total+dicio[x]
    return total