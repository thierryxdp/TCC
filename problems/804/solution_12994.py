def filtra_pares(tuple_a):
    
    #definindo os termos de tuple_a:
    a=tuple_a[0]
    b=tuple_a[1]
    c=tuple_a[2]
    d=tuple_a[3]
    
    #filtrando:
    if (a%2 == 0) and (b%2 != 0) and (c%2 != 0) and (d%2 != 0):
        tuple_a = (a)
    elif (a%2 == 0) and (b%2 == 0) and (c%2 != 0) and (d%2 != 0):
        tuple_a = (a, b)
    elif (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 != 0):
        tuple_a = (a, b, c)
    elif (a%2 == 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        tuple_a = (a, b, c, d)
    elif (a%2 != 0) and (b%2 != 0) and (c%2 != 0) and (d%2 != 0):
        tuple_a = ()
    elif (a%2 != 0) and (b%2 == 0) and (c%2 == 0) and (d%2 == 0):
        tuple_a = (b, c, d)
    elif (a%2 != 0) and (b%2 != 0) and (c%2 == 0) and (d%2 == 0):
        tuple_a = (c, d)
    elif (a%2 != 0) and (b%2 != 0) and (c%2 != 0) and (d%2 == 0):
        tuple_a = (d,)
    elif (a%2 != 0) and (b%2 == 0) and (c%2 != 0) and (d%2 == 0):
        tuple_a = (b, d)
    elif (a%2 == 0) and (b%2 != 0) and (c%2 == 0) and (d%2 != 0):
        tuple_a = (a, c)
 #retornando tuple_a:
    return tuple_a