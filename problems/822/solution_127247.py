def repetidos(l_numeros):
    i = 0
    a = 0
    while i < len(l_numeros):
        i += 1
        if l_numeros[i] in l_numeros:
            a = l_numeros.count(l_numeros[i]) + 1
            return a