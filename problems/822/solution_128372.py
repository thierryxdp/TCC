def repetidos(lista):
    """Essa função informa o números de vezes que um elemento da lista é igual ao anteterior
    list -> int"""
    repetidos = 0
    i = 0
    while i<len(lista):
        if lista[i] == lista[i-1]:
            repetidos = repetidos + 1
        i = i+1
    return repetidos