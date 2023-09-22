#Start your python function here
def filtra_pares(a,b,c,d):
    '''Retorna uma nova tupla com elementos pares da tupla original. int, int, int, int -> int'''
    x = (a,b,c,d)
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 ==0:
        return x
    if a%2 != 0 and b%2 == 0 and c%2 == 0 and d%2 == 0:
        return x[1:]
    if a%2 == 0 and b%2 != 0 and c%2 == 0 and d%2 == 0:
        return x[0:1]+x[2:]
    if a%2 == 0 and b%2 == 0 and c%2 != 0 and d%2 ==0:
        return x[0:2]+x[3:]
    if a%2 == 0 and b%2 == 0 and c%2 == 0 and d%2 != 0:
        return x[0:3]
    if a%2 == 0 and b%2 != 0 and c%2 != 0 and d%2 != 0:
        return (a,)
    if a%2 != 0 and b%2 != 0 and c%2 == 0 and d%2 ==0:
        return x[2:]
    if a%2 != 0 and b%2 == 0 and c%2 != 0 and d%2 != 0:
        return (b,)
    if a%2 != 0 and b%2 != 0 and c%2 == 0 and d%2 != 0:
        return (c,)
    if a%2 != 0 and b%2 != 0 and c%2 != 0 and d%2 == 0:
        return (d,)
    if a%2 == 0 and b%2 == 0 and c%2 != 0 and d%2 != 0:
        return x[0:2]
    if a%2 != 0 and b%2 == 0 and c%2 != 0 and d%2 == 0:
        return (b,d)
    if a%2 == 0 and b%2 != 0 and c%2 != 0 and d%2 == 0:
        return (a,d)
    if a%2 != 0 and b%2 == 0 and c%2 == 0 and d%2 != 0:
        return (b,c)
    if a%2 == 0 and b%2 != 0 and c%2 == 0 and d%2 != 0:
        return (a,c)
    if a%2 != 0 and b%2 != 0 and c%2 != 0 and d%2 != 0:
        return ()
    if a%2 == 0 and b%2 == 0 and c%2 == 0:
        return (a,b,c)
    if b%2 == 0 and c%2 == 0 and d%2 == 0:
        return x[1:]