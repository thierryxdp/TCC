def posLetra(frase, letra, posicao):
    index = 0
    lista = []
    for caracter in frase:
        if caracter == letra:
            lista.append(index)
        index = index + 1
    print(lista)

    if len(lista)>=posicao:
        return lista[posicao-1]
    else:
        return -1