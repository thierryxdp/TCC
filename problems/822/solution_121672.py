def repetidos(lista_numeros):
    """dada uma lista de números, a função retorna o número de vezes que um elemento da lista é igual ao elemento 
    anterior; list -> int"""
    i = 1
    j = 0
    while i < len(lista_numeros):
        if lista_numeros[i] == lista_numeros[i-1]:
            j = j + 1
        i = i + 1
    return j