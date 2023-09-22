def filtra_pares(t):
    '''Função que, dada uma tupla com 4 números, retorna uma outra tupla somente com os pares.
    tupla(int,int,int,int) --> tupla(int,int,int,int)'''
    n1 = t[0]
    n2 = t[1]
    n3 = t[2]
    n4 = t[3]
    
    if n1%2 == 0 and (not n2%2 == 0) and (not n3%2 == 0) and (not n4%2 == 0):
        return (n1,)
    elif n2%2 == 0 and (not n1%2 == 0) and (not n3%2 == 0) and (not n4%2 == 0):
        return (n2,)
    elif n3%2 == 0 and (not n2%2 == 0) and (not n1%2 == 0) and (not n4%2 == 0):
        return (n3,)
    elif n4%2 == 0 and (not n2%2 == 0) and (not n3%2 == 0) and (not n1%2 == 0):
        return (n4,)
    elif n1%2 == 0 and n2%2 == 0 and (not n3%2 == 0) and (not n4%2 == 0):
        return (n1,n2)
    elif n1%2 == 0 and n3%2 == 0 and (not n2%2 == 0) and (not n4%2 == 0):
        return (n1,n3)
    elif n1%2 == 0 and n4%2 == 0 and (not n3%2 == 0) and (not n2%2 == 0):
        return (n1,n4)
    elif n2%2 == 0 and n3%2 == 0 and (not n1%2 == 0) and (not n4%2 == 0):
        return (n2,n3)
    elif n2%2 == 0 and n4%2 == 0 and (not n3%2 == 0) and (not n1%2 == 0):
        return (n2,n4)
    elif n3%2 == 0 and n4%2 == 0 and (not n1%2 == 0) and (not n2%2 == 0):
        return (n3,n4)
    elif n1%2 == 0 and n2%2 == 0 and n3%2 == 0 and (not n4%2 == 0):
        return (n1,n2,n3)
    elif n1%2 == 0 and n2%2 == 0 and n4%2 == 0 and (not n3%2 == 0):
        return (n1,n2,n4)
    elif n1%2 == 0 and n3%2 == 0 and n4%2 == 0 and (not n2%2 == 0):
        return (n1,n3,n4)
    elif n2%2 == 0 and n3%2 == 0 and n4%2 == 0 and (not n1%2 == 0):
        return (n2,n3,n4)
    elif n1%2 == 0 and n2%2 == 0 and n3%2 == 0 and n4%2 == 0:
        return (n1,n2,n3,n4)
    else:
        return ()