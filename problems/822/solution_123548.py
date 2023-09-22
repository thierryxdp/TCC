def repetidos(lista):
    i=0
    k=i+1
    total = 0
    while k < len(lista):
        if lista[i] == lista[k]:
            total = total + 1
        i = i + 1  
        k= i +1
    return total