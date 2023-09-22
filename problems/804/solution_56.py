def filtra_pares(tupla):
    '''a partir de um tupla com quatro elementos inteiros, verifica quais deles sao pares e retorna-os em uma nova tupla
    int,int,int,int -> tuple'''
    if tupla[0] % 2 == 0:
        n1 = True
        N1 = tupla[0]
    else:
        n1 = False
    if tupla[1] % 2 == 0:
        n2 = True
        N2 = tupla[1]
    else:
        n2 = False
    if tupla[2] % 2 == 0:
        n3 = True
        N3 = tupla[2]
    else:
        n3 = False
    if tupla[3] % 2 == 0:
        n4 = True
        N4 = tupla[3]
    else:
        n4 = False
    if n1 and n2 and n3 and n4:
        return (N1,N2,N3,N4)
    elif n1 and n2 and n3:
        return (N1,N2,N3)
    elif n1 and n2 and n4:
        return (N1,N2,N4)
    elif n1 and n3 and n4:
        return (N1,N3,N4)
    elif n2 and n3 and n4:
        return (N2,N3,N4)
    elif n1 and n2:
        return (N1,N2)
    elif n1 and n3:
        return (N1,N3)
    elif n1 and n4:
        return (N1,N4)
    elif n2 and n3:
        return (N2,N3)
    elif n2 and n4:
        return (N2,N4)
    elif n3 and n4:
        return (N3,N4)
    elif n1:
        return (N1,)
    elif n2:
        return (N2,)
    elif n3:
        return (N3,)
    elif n4:
        return (N4,)
    else:
        return ()