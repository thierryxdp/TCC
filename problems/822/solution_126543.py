def repetidos(lista):
    '''
    Essa função recebe uma lista de números e retorna 
    o número de vezes que um elemento da lista é igual ao 
    seu anterior;
    list -> int
    '''
	dicionario = {i: lista.count(i) for i in lista}
    n_repetidos = 0
    for i in dicionario.values():
        if i != 1:
            n_repetidos += i - 1

    return n_repetidos