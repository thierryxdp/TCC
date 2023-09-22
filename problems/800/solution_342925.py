def total(lista,produtos):
    
    soma=[]
    lista=str(lista)
    for i in range(len(lista)):
        if lista in produtos:
            soma+=soma+produtos[lista[i]]
            
    return soma