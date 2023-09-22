def repetidos(lista):
    i=0
    k=i+1
    total = 0
    while i < len(lista):
        if lista[i] == lista[k]:
            total = total + 1
            return total