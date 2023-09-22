def repetidos(numeros):
    i = 0
    repetidos = 0
    j = 0
    while i < len(numeros):
        p1 = numeros[i-1]
        p2 = numeros[i]
        if p1 == p2:
            j += i
            repetidos = repetidos + 1
            i += i 
    return j