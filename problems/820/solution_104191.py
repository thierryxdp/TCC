def posLetra(frase, letra, posicao):
    index = 0
    lista = []
    for caracter in frase:
        if caracter == letra:
            lista.append(index)
        index = index + 1
        
    if len(lista)>0:
        return lista[posicao-1]
    else:
        return -1