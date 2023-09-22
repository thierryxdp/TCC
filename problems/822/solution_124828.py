def repetidos(lista_numeros):
    '''Retorna o números de vezes que um elemento da lista
       é igual ao anterior;
       list -> int'''
    acumulador = 0
    contador = 0
    while contador < len(lista_numeros) - 1:
        if lista_numeros[contador] == lista_numeros[contador + 1]:
            acumulador = acumulador + 1
        contador = contador + 1
    return acumulador