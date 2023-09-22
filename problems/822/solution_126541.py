def repetidos(lista):
    '''
    Essa função recebe uma lista de números e retorna 
    o número de vezes que um elemento da lista é igual ao 
    seu anterior;
    list -> int
    '''
def repetidos(lista):
    set1 = set(lista)
    n_repetido = len(lista) - len(set1)
    return n_repetido