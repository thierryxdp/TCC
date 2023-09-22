def repetidos(lista):
    q = 0
    
    for i in lista:
        a = lista[lista.index(i) - 1]
        
        if i == a:
            q += 1
    
    return q