def repetidos(lista):
    i=0
    contador=1
    while i<len(lista):
        if lista[i]==lista[i-1]:
            contador+=1
        i=i+1
    return contador