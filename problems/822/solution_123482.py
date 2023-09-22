def repetidos(lista_de_numeros):
    ocorrencias_repetidas = 0
    indice = 0
    for numero in lista_de_numeros:
        if lista_de_numeros[indice] == lista_de_numeros[indice-1]:
            ocorrencias_repetidas += 1
        if indice + 1 <= len(lista_de_numeros):
            indice += 1
    return ocorrencias_repetidas