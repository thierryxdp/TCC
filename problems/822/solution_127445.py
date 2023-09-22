def repetidos(lista):
    i=0
    a=0
    while i< len(lista):
        
        a+= list.count(lista,lista[i])
        i+=1
    return a