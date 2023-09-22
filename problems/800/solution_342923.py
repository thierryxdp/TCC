def total(lista,produtos):
    
    soma=[]
    x=dict.keys(produtos)
    for i in range(len(lista)):
        if lista in x:
            soma+=soma+produtos[lista[i]]
            
    return soma