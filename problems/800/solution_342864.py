def total(compra,preco):
    '''
    nessa fução foi verificado se o produto a ser comprado está no disponivel,
    se sim faz a soma dos valores.
    '''
    #list,dict -> float
    
    i = 0
    gasto = 0
    while i < len(compra):
         if compra[i] in preco:
            custo = dict.get(preco,compra[i])
            gasto = gasto + custo
            i+=1
        
    return round(gasto,2)