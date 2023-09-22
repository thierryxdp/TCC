def repetidos(x):
    i = 1
    cont = 0
    while i < len(x):
        if x[i] == x[i-1]:
        	cont += 1
        i += 1
    return cont