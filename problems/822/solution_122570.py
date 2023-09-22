def repetidos(lista):
    c = 0
    vezes = 0
    while c < len(lista)-1:
        if lista[c+1] == lista[c]:
            vezes += 1
        c += 1
    return vezes