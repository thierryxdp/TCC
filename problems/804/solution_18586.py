#Start your python function here
def filtra_pares(tup):
    '''Função que, dada uma tupla tup com quatro inteiros, retorna uma
    nova tupla contendo apenas os elementos pares da tupla inicial, mantendo
    a mesma ordem'''
    '''tuple -> tuple'''
    r1=int(tup[0])%2
    r2=int(tup[1])%2
    r3=int(tup[2])%2
    r4=int(tup[3])%2
    if r1==0 and r2==0 and r3==0 and r4==0:
        return (tup[0],tup[1],tup[2],tup[3])
    elif r1==0 and r2==0 and r3==0 and r4!=0:
        return (tup[0],tup[1],tup[2])
    elif r1==0 and r2==0 and r3!=0 and r4!=0:
        return (tup[0],tup[1])
    elif r1==0 and r2!=0 and r3!=0 and r4!=0:
        return (tup[0])
    elif r1==0 and r2==0 and r3!=0 and r4==0:
        return (tup[0],tup[1],tup[3])
    elif r1==0 and r2!=0 and r3==0 and r4==0:
        return (tup[0],tup[2],tup[3])
    elif r1==0 and r2!=0 and r3==0 and r4!=0:
        return (tup[0],tup[2])
    elif r1==0 and r2!=0 and r3!=0 and r4==0:
        return (tup[0],tup[3])
    elif r1!=0 and r2==0 and r3==0 and r4==0:
        return (tup[1],tup[2],tup[3])
    elif r1!=0 and r2==0 and r3!=0 and r4==0:
        return (tup[1],tup[3])
    elif r1!=0 and r2==0 and r3==0 and r4!=0:
        return (tup[1],tup[2])
    elif r1!=0 and r2==0 and r3!=0 and r4!=0:
        return (tup[1])
    elif r1!=0 and r2!=0 and r3==0 and r4==0:
        return (tup[2],tup[3])
    elif r1!=0 and r2!=0 and r3==0 and r4!=0:
        return (tup[2])
    elif r1!=0 and r2!=0 and r3!=0 and r4==0:
        return (tup[3])
    else:
        return ()