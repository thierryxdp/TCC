def repetidos(lista):
    l=[]
    i=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            list.append(l,lista[i])
        i=i+1
    return len(l)