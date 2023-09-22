def filtra_pares(a):
    '''Função que filtra e retorna os números pares da tupla de 4 números inteiros fornecida
    tupla(int, int, int, int) -> tupla(int,)'''
    a[0]=n1
    a[1]=n2
    a[2]=n3
    a[3]=n4
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n1,n2,n3,n4)
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n1,n2,n3)
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2==0:
        return (n1,n2,n4)
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return (n1,n2)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n1,n3,n4)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return (n1,n3)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return (n1,n4)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        return (n1)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n2,n3,n4)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n2,n3)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2==0:
        return (n2,n4)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return (n2)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n3,n4)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return (n3)
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return (n4)
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        return ()