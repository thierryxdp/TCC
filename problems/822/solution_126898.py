def repetidos(lista):
    i = 1
    contador = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            contador += 1
        i += 1
    return contador