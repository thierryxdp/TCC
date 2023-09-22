def filtra_pares(a,b,c,d):
    '''Função que retorna uma nova tupla contendo apenas
    os elemetos pares da tupla original, na mesma ordem em que
    se encontravam.
    a=int,b=int,c=int,d=int->tuple'''
    lista = []
 	if a%2 == 0:
        lista.append(a)
    if b%2 == 0:
        lista.append(b)
    if c%2 == 0:
        lista.append(c)
    if d%2 == 0:
        lista.append(d)
    return tuple(lista)