def repetidos(numeros):
    i = 0
    repetidos = 0
    p1 = numeros[i+1]
    p2 = numeros[i]
    j = 0
    while i < len(numeros):
        if p1 == p2:
            j += i
            repetidos = repetidos + 1
        i = i + 1
    return j