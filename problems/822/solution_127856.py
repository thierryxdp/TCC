def repetidos(lista):
    """Função que recebe uma lista de números como entrada,
    e retorna o número de vezes que um elemento da lista é
    igual ao elemento anterior;
    list -> int"""
    k = 0
    r = 0
    while k + 1 < len(lista):
        if lista[k] == lista[k +1]:
            r = r + 1
        k = k + 1
    return r