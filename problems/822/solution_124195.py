def repetidos(lista):
    i=7
    r=[]
    while i < len(lista):
        if lista[i]==lista[i-1]:
            r.append(lista[i])
            
    return len(r)