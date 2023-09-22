def total(lista,produtos):
    
    lista=tuple(list)
    soma=0
    for i in range(len(lista)):
        if lista in produtos:
            soma+=soma+produtos[lista[i]]
            
    return soma