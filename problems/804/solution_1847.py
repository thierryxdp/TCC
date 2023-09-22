def filtra_pares(a,b,c,d):
    '''retorna a funcao de uma tupla com quatro elementos inteiros pares, sendo a,b,c,d numeros inteiros'''
    filta= a
    filtb= b
    filtc= c
    filtd= d
    para= filta%2
    parb= filtb%2
    parc= filtc%2
    pard= filtd%2
    if (para==0 and parb==0 and parc==0 and pard!=0):
        return (filta,filtb,filtc)
    elif (para==0 and parb!=0 and parc==0 and pard!=0):
        return (filta,filtc)
    elif (para==0 and parb==0 and parc!=0 and pard!=0):
        return (filta,filtb)
    elif (para!=0 and parb!=0 and parc!=0 and pard==0):
        return (filtd,)
    elif (para==0 and parb!=0 and parc==0 and pard==0):
        return (filta,filtc,filtd)
    elif (para!=0 and parb!=0 and parc!=0 and pard!=0):
        return ()
    elif (para!=0 and parb!=0 and parc==0 and pard==0):
        return (filtc,filtd)
    elif (para!=0 and parb==0 and parc==0 and pard!=0):
        return (filtb,filtc)
    elif (para==0 and parb==0 and parc==0 and pard==0):
        return (filta,filtb,filtc,filtd)
    elif (para!=0 and parb==0 and parc==0 and pard==0):
        return (filta,filtb,filtc)