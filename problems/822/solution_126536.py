def repetidos(lista):
    '''
    Essa função recebe uma lista de números e retorna 
    o número de vezes que um elemento da lista é igual ao 
    seu anterior;
    list -> int
    '''
    def repetidos(lista):
    frente = 1
    n_repetido = 0

    for i in range(0, len(lista)):
        if lista[i] == lista[frente]:
            n_repetido += 1
            continue
        frente += 1
    return n_repetido