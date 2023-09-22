def filtra_pares(a):
    '''funcao tem entrada de 4 elementos inteiros e saida apenas dos elementos pares'''
    '''int=>???'''
    b=()
    if a[0]% 2 == 0:
        b = b + (a[0],)
    if a[1]% 2 == 0:
        b = b + (a[1],)
    if a[2]% 2 == 0:
        b = b + (a[2],)
    if a[3]% 2 == 0:
        b = b + (a[3],)
    return b