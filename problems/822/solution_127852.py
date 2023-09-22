def repetidos (lista_numeros):
    '''retorna o número de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    i = 1
    contador = 0
    numero_anterior = lista_numeros[0]
    while i < len(lista_numeros):
        if lista_numeros[i] == numero_anterior:
            contador = contador + 1
        numero_anterior = lista_numeros[i]
    return contador