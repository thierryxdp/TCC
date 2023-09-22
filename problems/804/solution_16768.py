def filtra_pares(i1,i2,i3,i4):
    '''retorna apenas os numeros pares dados nas entradas
    entradas:tupla com int,int,int,int
    saida:tupla vazia ou tupla com 1 a 4 int'''
    if i1%2==0 and i2%2!=0 and i3%2!=0 and i4%2!=0:
        return (i1,)
    elif i1%2!=0 and i2%2==0 and i3%2!=0 and i4%2!=0:
        return (i2,)
    elif i1%2!=0 and i2%2!=0 and i3%2==0 and i4%2!=0:
        return (i3,)
    elif i1%2!=0 and i2%2!=0 and i3%2!=0 and i4%2==0:
        return (i4,)
    elif i1%2==0 and i2%2==0 and i3%2!=0 and i4%2!=0:
        return (i1,i2)
    elif i1%2==0 and i2%2!=0 and i3%2==0 and i4%2!=0:
        return (i1,i3)
    elif i1%2==0 and i2%2!=0 and i3%2!=0 and i4%2==0:
        return (i1,i4)
    elif i1%2!=0 and i2%2==0 and i3%2==0 and i4%2!=0:
        return (i2,i3)
    elif i1%2!=0 and i2%2==0 and i3%2!=0 and i4%2==0:
        return (i2,i4)
    elif i1%2!=0 and i2%2!=0 and i3%2==0 and i4%2==0:
        return (i3,i4)
    elif i1%2==0 and i2%2==0 and i3%2==0 and i4%2!=0:
        return (i1,i2,i3)
    elif i1%2==0 and i2%2==0 and i3%2!=0 and i4%2==0:
        return (i1,i2,i4)
    elif i1%2==0 and i2%2!=0 and i3%2==0 and i4%2==0:
        return (i1,i3,i4)
    elif i1%2!=0 and i2%2==0 and i3%2==0 and i4%2==0:
        return (i2,i3,i4)
    elif i1%2==0 and i2%2==0 and i3%2==0 and i4%2==0:
        return (i1,i2,i3,i4)
    else:
        return ()