def repetidos(lista):
    i=0
    a=0
    while i< len(lista):
        i=i+1
        a+= list.count(lista,lista[i])
    return a