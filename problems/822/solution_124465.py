def repetidos(lista):
    """Função que dado uma lista de números retorna
    a quantidade de vezes que um elemento da lista
    é igual ao elemento anterior.lsit -> int"""
    i = 0
    r = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            r = r + 1
        i = i + 1
    return r