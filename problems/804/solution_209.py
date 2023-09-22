def filtra_pares(tupla_inteiros):
    """Entre com uma tupla de 4 números inteiros quaisquer
    -não se esqueça de colocá-los entre ()-
    para que a função retorne os números pares
    na ordem em que foram passados.
    tupla(int, int, int, int)->tupla"""
    pares=()
    (a,b,c,d)=tupla_inteiros
    y=(bool(not a%2), bool(not b%2), bool(not c%2), bool(not d%2))
    #Todos pares
    if y[0] and y[1] and y[2] and y[3]:
        pares = pares + (a,b,c,d)
        return pares
    #a é par, o resto é ímpar
    elif y[0] and (not y[1]) and (not y[2]) and (not y[3]):
        pares = pares +(a,)
        return pares
    #Só b é par
    elif (not y[0]) and (y[1]) and (not y[2]) and (not y[3]):
        pares = pares +(b,)
    #Só c é par
    elif (not y[0]) and (not y[1]) and (y[2]) and (not y[3]):
        pares = pares +(c,)
    #Só d é par
    elif (not y[0]) and (not y[1]) and (not y[2]) and (y[3]):
        pares = pares +(d,)
    #a e b são pares, o resto é ímpar
    elif y[0] and (y[1]) and (not y[2]) and (not y[3]):
        pares = pares +(a,b)
    #a e c são pares, o resto é ímpar
    elif y[0] and (not y[1]) and (y[2]) and (not y[3]):
        pares = pares +(a,c)
    #a e d são pares, o resto é ímpar
    elif y[0] and (not y[1]) and (not y[2]) and (y[3]):
        pares = pares +(a,d)
    #b e c são pares, o resto é ímpar
    elif (not y[0]) and (y[1]) and (y[2]) and (not y[3]):
        pares = pares +(b,c)
    #b e d são pares
    elif (not y[0]) and (y[1]) and (not y[2]) and (y[3]):
        pares = pares +(b,d)
    #c e d são pares
    elif (not y[0]) and (not y[1]) and (y[2]) and (y[3]):
        pares = pares +(c,d)
    #a, b, c são pares
    elif y[0] and (y[1]) and (y[2]) and (not y[3]):
        pares = pares +(a,b,c)
    #a,b,d são pares
    if y[0] and y[1] and (not y[2]) and y[3]:
        pares = pares + (a,b,d)
    #a, c, d são pares
    if y[0] and (not y[1]) and y[2] and y[3]:
        pares = pares + (a,c,d)
        return pares
    #b,c, d são pares
    if not(y[0]) and y[1] and y[2] and y[3]:
        pares = pares + (b,c,d)
        return pares
    #Nenhum é par
    else:
        return pares#Start your python function here