def repetidos(lista_de_numeros):
    i = 0
    numeros_repetidos = []
    copia = lista_de_numeros[:]
    
    while i < len(lista_de_numeros):
        if lista_de_numeros[i] in copia:
            numeros_repetidos =+ [(list.count(lista_de_numeros[i], lista_de_numeros))]
        i += 1
        list.sort(numeros_repetidos)
    return numeros_repetidos[-1]