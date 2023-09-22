def repetidos(lista):
    vezes = 0
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1]:
            vezes += 1
    return vezes