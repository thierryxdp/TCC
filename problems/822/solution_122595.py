def repetidos(lista_numeros):
    '''Função que recebe uma lista de números e retorna
    o número de vezes que um elemento dessa lista é igual 
    ao elemento anterior.
    Dados de entrada: list
    Valor de saída: int
    '''
    indice_lista = 0
    numero_de_repeticoes = 0
    while indice_lista < len(lista_numeros)-1:
        if lista_numeros[indice_lista + 1] == lista_numeros[indice_lista]:
            numero_de_repeticoes = numero_de_repeticoes + 1
        indice_lista += 1
    return numero_de_repeticoes