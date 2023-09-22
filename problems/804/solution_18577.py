#Start your python function here
def filtra_pares([a,b,c,d]):
    '''Função que, dada uma tupla com quatro inteiros a,b,c e d, retorna uma
    nova tupla contendo apenas os elementos pares da tupla inicial, mantendo
    a mesma ordem'''
    '''tuple -> tuple'''
    r1=a%2
    r2=b%2
    r3=c%2
    r4=d%2
    if r1==0 and r2==0 and r3==0 and r4==0:
        return (a,b,c,d)
    elif r1==0 and r2==0 and r3==0 and r4!=0:
        return (a,b,c)
    elif r1==0 and r2==0 and r3!=0 and r4!=0:
        return (a,b)
    elif r1==0 and r2!=0 and r3!=0 and r4!=0:
        return (a)
    elif r1==0 and r2==0 and r3!=0 and r4==0:
        return (a,b,d)
    elif r1==0 and r2!=0 and r3==0 and r4==0:
        return (a,c,d)
    elif r1==0 and r2!=0 and r3==0 and r4!=0:
        return (a,c)
    elif r1==0 and r2!=0 and r3!=0 and r4==0:
        return (a,d)
    elif r1!=0 and r2==0 and r3==0 and r4==0:
        return (b,c,d)
    elif r1!=0 and r2==0 and r3!=0 and r4==0:
        return (b,d)
    elif r1!=0 and r2==0 and r3==0 and r4!=0:
        return (b,c)
    elif r1!=0 and r2==0 and r3!=0 and r4!=0:
        return (b)
    elif r1!=0 and r2!=0 and r3==0 and r4==0:
        return (c,d)
    elif r1!=0 and r2!=0 and r3==0 and r4!=0:
        return (c)
    elif r1!=0 and r2!=0 and r3!=0 and r4==0:
        return (d)
    else:
        return ()