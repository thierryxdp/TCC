def total(lista,produtos):
    
    soma=[]
    
    for i in range(len(lista)):
        x=lista=str(lista)
        if lista in produtos:
            soma+=produtos[lista[i]]
            
    return x