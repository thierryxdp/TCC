def repetidos(lista):
    x = 0
    i = 0
    while x < len(lista):
        if lista[i + 1] == lista[i]:
            resultado += 1
        x += 1
        i += 1
    return resultado