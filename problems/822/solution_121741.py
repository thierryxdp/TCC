def repetidos(lista):
    
    """Essa funcao retorna o numero de vezes que um elemento da lista de entrada e igual ao elemento anterior;
    list -> int"""

    i = 0
    contador = 0

    while i < len(lista):
        if lista[i-1] == lista[i]:
            contador = contador + 1
        i = i + 1
    return contador