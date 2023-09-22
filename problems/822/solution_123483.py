def repetidos(lista_de_numeros):
    '''retorna a quantidade de vezes que o numero da lista é igual ao numero anterior.
    list -> int'''
    ocorrencias_repetidas = 0
    indice = 0
    for numero in lista_de_numeros:
        if lista_de_numeros[indice] == lista_de_numeros[indice-1]:
            ocorrencias_repetidas += 1
        if indice + 1 <= len(lista_de_numeros):
            indice += 1
    return ocorrencias_repetidas