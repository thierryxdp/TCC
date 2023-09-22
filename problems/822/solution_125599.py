def repetidos(lista):
    """função que retorna as vezes que um elemento é igual ao anterior
    list -> int"""
    e = lista
    i = 0
    n = 0
    while i <= len(e):
        if int(e[i-1]) == int(e[i]):
            n = n + 1
        i = i + 1
    return n