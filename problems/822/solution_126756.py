def repetidos(lista):
    i=0
    count=0
    while i < len(lista):
        if lista[i]=lista[i-1]:
            count+=1
    return count