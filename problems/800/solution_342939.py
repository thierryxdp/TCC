def total(lista,produtos):
    
    soma=0
    
    for i in range(len(produtos)):
        lista=str(lista)
        if lista in produtos:
            soma+=soma+produtos[lista[i]]
            
    return soma