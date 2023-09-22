def repetidos(lista):
    contador = 0
    a = len(lista)-1
    for x in range(a):
        if lista[x+1] == lista[x]:
            contador += 1
    return contador