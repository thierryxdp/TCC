def filtra_pares(tupla):
    '''retorna a funcao de uma tupla com quatro elementos inteiros pares, sendo a,b,c,d numeros inteiros'''
    a,b,c,d= tupla
    para= a%2
    parb= b%2
    parc= c%2
    pard= d%2
    if (para==0 and parb==0 and parc==0 and pard!=0):
        return (a,b,c)
    elif (para==0 and parb!=0 and parc==0 and pard!=0):
        return (a,c)
    elif (para==0 and parb==0 and parc!=0 and pard!=0):
        return (a,b)
    elif (para!=0 and parb!=0 and parc!=0 and pard==0):
        return (d,)
    elif (para==0 and parb!=0 and parc==0 and pard==0):
        return (a,c,d)
    elif (para!=0 and parb!=0 and parc!=0 and pard!=0):
        return ()
    elif (para!=0 and parb!=0 and parc==0 and pard==0):
        return (c,d)
    elif (para!=0 and parb==0 and parc==0 and pard!=0):
        return (b,c)
    elif (para==0 and parb==0 and parc==0 and pard==0):
        return (a,b,c,d)
    elif (para!=0 and parb==0 and parc==0 and pard==0):
        return (b,c,d)