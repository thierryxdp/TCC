def repetidos(lista):
    contador=0
    i=0
    a=1
    while a<len(lista):
        if lista[a]==lista[contador]:
            contador+=1
            i+=1
            a+=1
        else:
            a+=1
            contador+=1
    return i