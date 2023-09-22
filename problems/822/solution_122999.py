def repetidos(lista):
    contador = 0
    i = 1
    while i < len(lista):
        print(lista[i-1])
        if lista[i] == lista[i-1]:
            contador += 1
        i += 1
    return contador