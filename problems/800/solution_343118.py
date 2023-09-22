def total(lista_compras, produtos):
    '''
    Funcao que recebe uma lista e um dicionario. A funcao retorna o custo total dos produtos que estão na lista de compras
    list, dict -> float
    '''  
    total = 0
    for item in lista_compras:
        if item in produtos.keys():
            total = total + produtos[item]
            
    return round(total,2)