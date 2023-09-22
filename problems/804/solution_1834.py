def filtra_pares(a,b,c,d):
    '''retorna a funcao de uma tupla com quatro elementos inteiros pares, sendo a,b,c,d numeros inteiros'''
    filt1= a
    filt2= b
    filt3= c
    filt4= d
    para= a%2
    parb= b%2
    parc= c%2
    pard= d%2
    if (para==0 and parb==0 and parc==0 and pard!=0):
        return (filt1,filt2,filt3)
    elif (para==0 and parb!=0 and parc==0 and pard!=0):
        return (filt1,filt3)
    elif (para==0 and parb==0 and parc!=0 and pard!=0):
        return (filt1,filt2)
    elif (para!=0 and parb!=0 and parc!=0 and pard==0):
        return (filt4,)
    elif (para==0 and parb!=0 and parc==0 and pard==0):
        return (filt1,filt3,filt4)
    elif (para!=0 and parb!=0 and parc!=0 and pard!=0):
        return ()
    elif (para!=0 and parb!=0 and parc==0 and pard==0):
        return (filt3,filt4)
    elif (para!=0 and parb==0 and parc==0 and pard!=0):
        return (filt2,filt3)
    elif (para==0 and parb==0 and parc==0 and pard==0):
        return (filt1,filt2,filt3,filt4)
    elif (para!=0 and parb==0 and parc==0 and pard==0):
        return (filt2,filt3,filt4)