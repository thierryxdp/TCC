def repetidos (lista):
    a = 1
    b = 0
    elementos = 0
    while b < len(lista)-1:
        if lista[a] == lista[b]:
            a += 1
            b += 1
            elementos += 1
            return elementos