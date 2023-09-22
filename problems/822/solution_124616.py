def repetidos(lista):
    cont = 0
    i = 0
    while i < len(lista):
        if i == 0:
            i += 1
            continue
        else:
            if lista[i] == lista[i-1]:
                cont += 1
        i += 1
    return cont