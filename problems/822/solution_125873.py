def repetidos(x):
    i = 0
    cont = 0
    while i < len(x):
        if x[i] == x[i-1]:
        cont += 1
    return cont