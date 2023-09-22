def total(lista,produtos):
    
    soma=0
    x=dict.keys(produtos)
    for i in range(len(lista)):
        if lista in x:
            soma+=soma+produtos[lista[i]]
            
    return soma