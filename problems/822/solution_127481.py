def repetidos(lista):
    i=0
    a=0
    while i<len(lista)-1:
        if lista[i]==lista[i+1]:
            a+=1
            i+=1

    return a