def filtra_pares(a,b,c,d):
    '''retorna uma nova tupla com os elementos pares de uma tupla de 4 elementos inteiros de entrada, na ordem que aparecem nela
    -> tup '''
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        print (a,b,c,d)
    if a%2 == 0 and b%2 != 0 and c%2 == 0 and d%2 == 0:
        print (a,c,d)
    if a%2 == 0 and b%2 == 0 and c%2 != 0 and d%2 == 0:
        print (a,b,d)
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 != 0:
        print (a,b,c)
    if a%2 != 0 and b%2 != 0 and c%2 == 0 and d%2 == 0:
        print (c,d)
    if a%2 != 0 and b%2 == 0 and c%2 != 0 and d%2 == 0:
        print (b,d)
    if a%2 != 0 and b%2 == 0 and c%2 == 0 and d%2 != 0:
        print (b,c)
    if a%2 == 0 and b%2 != 0 and c%2 != 0 and d%2 == 0:
        print (a,d)
    if a%2 == 0 and b%2 != 0 and c%2 == 0 and d%2 != 0:
        print (a,c)
    if a%2 == 0 and b%2 == 0 and c%2 != 0 and d%2 == 0:
        print (a,b)
    else: print ("()")