def filtra_pares (tup):
    '''funcao que retorna uma tupla apenas com os elementos pares da tupla dada
    tuple -> tuple'''
    somatupla = ()
    if tup[0]%2==0:
        somatupla = somatupla + (tup[0],)
    if tup[1]%2==0:
        somatupla = somatupla + (tup[1],)
    if tup[2]%2==0:
        somatupla = somatupla + (tup[2],)
    if tup[3]%2==0:
        somatupla = somatupla + (tup[3],)
    return somatupla