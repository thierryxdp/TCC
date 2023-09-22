def repetidos(lista):
    r=0
    i=0
    lista2=[]
    while i < len(lista):
        lista2.insert(lista.count(lista[i]))
        i = i+1
    return max(lista2)