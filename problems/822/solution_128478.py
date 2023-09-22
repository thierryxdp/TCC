def repetidos (lista):
    '''Retorna a quantidade vezes que dois caracteres seguidos são iguais list->str'''
    i = 0
    q = 0
    while lista[i]>len(lista):
        if lista[i] == lista[i + 1]:
        q = q + 1
    return q