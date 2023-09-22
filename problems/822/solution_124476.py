def repetidos(lista):
    i=0
    num=0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            num +=1
        i+=1
    return num