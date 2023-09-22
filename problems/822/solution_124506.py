def repetidos(lista):
    tamanho = len(lista)
    i = 1
    contador = 0
    while i < tamanho:
        if lista[i-1] == lista[i]:
            contador += 1
        i += 1
    return contador