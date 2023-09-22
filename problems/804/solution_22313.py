def filtra_pares (a,b,c,d):
    '''retorna uma nova tupla com os inteiros pares de uma tupla com 4 elementos inteiros de entrada
    tup -> tup'''
    tupla = ()
    if a%2==0:
        tupla.append(a)
    if b%2==0:
        tupla.append(b)
    if c%2==0:
        tupla.append(c)
    if d%2==0:
        tupla.append(d)