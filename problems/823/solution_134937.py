def faltante(n):
    # n é uma lista com os numeros
    i = 0
    while i < len(n):
        if i+1 not in (n):
            return i+1
        i = i +1
    return i+1