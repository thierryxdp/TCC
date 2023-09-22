def repetidos(lista):
    '''Função que retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
    list -> int'''
    i = 1
    score = 0
    while i<len(lista):
        if lista[i-1] == lista[i]:
            score = score + 1 
        i = i + 1
    return score