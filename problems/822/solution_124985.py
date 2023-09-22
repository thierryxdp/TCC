def repetidos(lista):
    r=0
    i=0
    lista2=[]
    while i < len(lista):
        repeticao = lista.count(lista[i])
        lista2.insert(repeticao)
        i = i+1
    return max(lista2)