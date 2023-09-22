def faltando(L):
    '''função que dada uma lista L retorna o numero que está
    faltando na sequencia'''
    contador = 0
    while L[contador] != (L[contador - 1] + 1):
        contador = contador + 1
    return L[contador] + 1