def repetidos(lista):
    i=0
    while i<len(lista):
        if lista[i] == lista[i+1]:
            res += 1
        i+=1
        return res