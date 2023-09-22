def repetidos(numeros):
    i = 1
    repetidos = 0
    j = 0
    while i < len(numeros):
        p1 = i
        p2 = i + 1
        if p1 == p2:
            repetidos += 1
        i = i + 1
    return repetidos