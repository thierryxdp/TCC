def repetidos(numeros):
    i = 0
    repetidos = 0
    j = 0
    while i < len(numeros):
        p1 = numeros[i - 1]
        p2 = numeros
        if p1 == p2:
            j += 1
            repetidos = repetidos + 1
        i = i + 1
    return j