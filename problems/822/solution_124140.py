def repetidos(lista):
    q = 0
    
    for i in lista:
        a = lista[lista.index(i)]
        
        if i == a:
            q += 1
    
    return q