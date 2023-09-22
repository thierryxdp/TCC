def filtra_pares(a,b,c,d):
	'''
        dados 4 inteiros faz a filtragem de quais deles são pares
        e retorna-os na ordem que aparecem
        int, int, int, int -> str
    '''
    if a%2 == 0:
        pares = str(a)
    if b%2 == 0:
        pares = pares + ',' + str(b)
    if c%2 == 0:
        pares = pares + ',' + str(c)
    if d%2 == 0:
        pares = pares + ',' + str(d)
    if a%2 != 0 and b%2 != 0 and c%2 != 0 and d%2 != 0:
        pares = 'Não há inteiros pares'
    return pares