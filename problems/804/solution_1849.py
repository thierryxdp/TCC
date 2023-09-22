def filtra_pares((a,b,c,d)):
    '''retorna a funcao de uma tupla com quatro elementos inteiros pares, sendo a,b,c,d numeros inteiros'''
    para= a%2
    parb= b%2
    parc= c%2
    pard= d%2
    if (para==0 and parb==0 and parc==0 and pard!=0):
        return (filt1)
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