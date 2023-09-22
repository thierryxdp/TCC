def repetidos (lista):
    '''Recebe como entrada uma lista de números, e retorna
    o número de vezes que um elemento da lista é igual ao
    elemento anterior.
    list -> int'''
    resp = 0
    i = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            resp = resp + 1
        i += 1
    return resp