def repetidos(lista):
    i=0
    num=0
    while i<len(lista):
        if lista[i]==lista[1:-1]:
            num+=1
        i+=1
    return num