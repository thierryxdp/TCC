def repetidos(lista):
    qtd = 0
    for x in range (0,len(lista)-1):
        if (lista[x] == lista[x+1]):
            qtd = qtd + 1
    return qtd