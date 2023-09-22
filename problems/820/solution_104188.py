def posLetra(frase, letra, posicao):
    index = 0
    lista = []
    for caracter in frase:
        if caracter == letra:
            lista.append(index)
        index = index + 1
        
    return lista[posicao-1]