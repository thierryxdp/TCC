def filtra_pares(t):
	'''
dado uma tupla com 4 inteiros como elementos, retorna só os
elementos pares
dados de entrada: tuple
dados de retorno: tuple
	'''
    a = t[0] 
    b = t[1] 
    c = t[2]
    d = t[3]
    x = t[0] % 2 == 0
    y = t[1] % 2 == 0
    z = t[2] % 2 == 0
    w = t[3] % 2 == 0
    if x and not y and not z and not w:
        return (a,)
    elif y and not x and not z and not w:
        return (b,)
    elif z and not x and not y and not w:
        return (c,)
    elif w and not x and not y and not z:
        return (d,)
    elif x and y and not z and not w:
        return (a,b)
    elif x and z and not y and not w:
        return (a,c)
    elif x and w and not y and not z:
        return (a,d)
    elif x and y and z and not w:
        return (a,b,c)
    elif x and y and w and not z:
        return (a,b,d)
    elif x and z and w and not y:
        return (a,c,d)
    elif y and z and w and not x:
        return (b,c,d)
    elif y and z and not w and not x:
        return (b,c)
    elif y and w and not z and not x:
        return (b,d)
    elif w and z and not x and not y:
        return (c,d)
	elif x and y and z and w:
        return (a,b,c,d)
    else:
        return ()