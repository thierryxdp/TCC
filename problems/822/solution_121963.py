def repetidos(lista_de_numeros):
    """Esta é a função que dado uma lista de números retorna o número de vezes que um elemento da lista é igual ao elemento anterior; list -> int"""
    i = 0
    n = 0

    while i < len(lista_de_numeros):
        if lista_de_numeros[i] == lista_de_numeros[i -1]:
            
            i = i + 1
            n = n + 1
            
        else:
            
            i = i + 1

    return n