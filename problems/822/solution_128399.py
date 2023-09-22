def repetidos(lista):
    i = 0
    s = []
    while i<len(lista):
        if lista[i] == lista[i+1]:
            s = s + [1]
        i = i +1
    return sum(s)