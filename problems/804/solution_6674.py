def filtra_pares(tupla):
    '''recebe uma tuple de parâmetros inteiros e retorna uma nova tuple
    com os parâmetroz pares da tuple original'''
    NovaTupla = ()
    t0 = tupla[0]%2
    if t0 == 0:
        aux = NovaTupla + (tupla[0],)
        NovaTupla = aux
    t1 = tupla[1]%2
    if t1 == 0:
        aux = NovaTupla + (tupla[1],)
        NovaTupla = aux
    t2 = tupla[2]%2
    if t2 == 0:
        aux = NovaTupla + (tupla[2],)
        NovaTupla = aux
    t3 = tupla[3]%2
    if t3 == 0:
        aux = NovaTupla + (tupla[3],)
        NovaTupla = aux
    return NovaTupla