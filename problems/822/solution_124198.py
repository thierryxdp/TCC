def repetidos(lista):
    i=1
    r=[]
    while i < len(lista):
        if lista[i]==lista[i-1]:
            r.append(lista[i])
            i=i+1
    return len(r)