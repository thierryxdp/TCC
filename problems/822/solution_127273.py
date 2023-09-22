def repetidos(lista_numeros):
    '''
    dada uma lista como argumento, retorna o numero de 
    vezes que um elemento da lista é igual ao seu
    antecessor
    dados de entrada: list
    retorna: int
    '''
    contador = 1
    contador_repeticoes = 0
    while contador < len(lista_numeros):
        if lista_numeros[contador] == lista_numeros[contador - 1]:
            contador_repeticoes = contador_repeticoes + 1
        contador = contador + 1
    return contador_repeticoes