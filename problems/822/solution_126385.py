def repetidos(lista):
    """Recebe um lista de números, depois retorna retorna o número de vezes que um elemento
    é igual ao elemento anterior; list -> int"""
    x = 1
    tamanho = len(lista)
    y = 0
    while x < tamanho:
        if lista[x] == lista[x-1]:
            y = y+1
        x = x+1
    return y