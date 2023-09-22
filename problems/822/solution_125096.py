def repetidos(lista):
    i=0
    qtd_repetidos = 0
    while i < (len(lista)):
        if lista[i] == lista[i-1]:
            qtd_repetidos = qtd_repetidos + 1
        else:
            qtd_repetidos = qtd_repetidos + 0
        i = i + 1
    return qtd_repetidos