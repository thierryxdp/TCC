def repetidos(numeros):
    """Funcao que retorna o numero de vezes que um elemento da lista de
    numeros eh igual ao elemento anterior; list -> int"""

    i = 0
    contador = 0

    while i < len(numeros)-1:
        if numeros[i] == numeros[i+1]:
            contador = contador + 1 
        i = i + 1
    return contador