def repetidos(numeros):
    '''retorna o número de vezes que um elemento da lista é igual ao elemento anterior; list -> int'''

    contador = 0
    
    for i in range(0,len(numeros)):
        if numeros[i] == numeros[i-1]:
            contador = contador + 1
    return contador