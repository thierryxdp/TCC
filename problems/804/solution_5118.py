def filtra_pares(n):
    """Retona na sequência original os números da entrada que são pares;
    int,int,int,int->int,..."""
    n1=n[0]
    n2=n[1]
    n3=n[2]
    n4=n[3]
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n1,n2,n3,n4)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2!=0:
        return (n1,)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return(n2,)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return(n3,)
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return(n4,)
    elif n1%2==0 and n2%2==0 and n3%2!=0 and n4%2!=0:
        return (n1,n2)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2!=0:
        return (n1,n3)
    elif n1%2==0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return(n1,n4)
    elif n1%2==0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n1,n2,n3)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n1,n3,n4)
    elif n1%2==0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n1,n2,n4)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2!=0:
        return (n2,n3)
    elif n1%2!=0 and n2%2==0 and n3%2!=0 and n4%2==0:
        return (n2,n4)
    elif n1%2!=0 and n2%2!=0 and n3%2==0 and n4%2==0:
        return (n3,n4)
    elif n1%2!=0 and n2%2==0 and n3%2==0 and n4%2==0:
        return (n2,n3,n4)
    elif n1%2!=0 and n2%2!=0 and n3%2!=0 and n4%2==0:
        return 4%2
    else:
        return ()