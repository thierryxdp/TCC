def repetidos(l):
    '''recebe uma lista de números(l), e retorna o número de vezes que um elemento da lista
    é igual ao elemento anterior; list -> int'''
    l1 = []
    l2 = l[:]
    contagem = 0
    while contagem < len(l2) - 1:
        if l[0] == l[1]:
            l1.append(l[0])
        	del l[0]
        else:
            del l[0]
        contagem = contagem + 1
    return len(l1)