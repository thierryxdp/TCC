def filtra_pares(a):
    '''filtra a tupla de 4 números a, retornando uma tupla somente com os números pares dela:
    tupla(int, int, int, int) --> tupla(int,)'''
    n1=a[0]
    n2=a[1]
    n3=a[2]
    n4=a[3]
    
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n1,n2,n3,n4)
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n1,n2,n3)
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2==0:
        return (n1,n2,n4)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n1,n3,n4)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n2,n3,n4)
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return (n1,n2)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return (n1,n3)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return (n1,n4)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n2,n3)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2==0:
        return (n2,n4)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n3,n4)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        return (n1,)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return (n2,)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return (n3,)
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return (n4,)
    else:
        return ()