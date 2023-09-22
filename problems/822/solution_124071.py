def repetidos(lista):
    i = 0
    n = 0
    while i<len(lista):
        if lista[i]==range(len(lista)+1):
            n = n + 1
        i = i + 1
    return n