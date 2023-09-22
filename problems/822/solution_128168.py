def repetidos(lista):
    """Funcao que retorna o numero de vezes que o elemento
    é o mesmo que o anterior. list->int"""
    i = 1
    j = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            j = j + 1
        i = i + 1
    return j