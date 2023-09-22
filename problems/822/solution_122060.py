def repetidos(lista):
    i=1
    contador= 0
    while i<len(lista)-2:
        if lista[i]==lista[i-1]:
            contador+=1
        i+=1
    return contador