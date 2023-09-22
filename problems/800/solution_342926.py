def total(lista,produtos):
    
    soma=[]
    
    for i in range(len(lista)):
        lista=str(lista)
        if lista in produtos:
            soma+=soma+produtos[lista[i]]
            
    return soma