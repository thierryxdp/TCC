def faltante(l):
    '''função que, dada uma lista(l) de 
    N inteiros de 1 a N, retorna o numero, dentro deste intervalo,
    que está faltando. list ->int'''
    i=1
    atual=1
    while i in l:
        if i in l:
            i=atual
            atual=atual+1
    return i