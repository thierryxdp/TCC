def repetidos(lista):
    '''Função que dada uma lista de números, retorna o número de vezes de um elemento da lista é igual ao elemento anterior: list -> int'''
    i = 1
    cnt = 0
    while i < len(lista):
        if lista[i-1] == lista[i]:
            cnt += 1
        i += 1
    return cnt