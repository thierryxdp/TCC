def filtra_pares (a, b, c, d):
    '''essa função retorna uma nova tupla apenas com os numeros pares da tupla original
    tupla (int) -> tupla (int)'''
 
    x=() 
    if a /2 == 0:
        x= x + (a, )
    else:
        x=x
    if b/2 == 0:
        x = x +(b, )
    else:
        x=x
    if c /2 ==0:
        x = x+ (c, )
    else:
        x=x
    if d/2 ==0:
        x = x + (d, )
    else:
        x=x
        return x