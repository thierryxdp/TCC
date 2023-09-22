def repetidos(lista):
    
    l1=[]
    c=0
    while c<len(lista)-1:
        if lista[c]==lista[c+1]:
            list.append(l1,lista[c])
        c=c+1
    return len(l1)