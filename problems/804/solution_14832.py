def filtra_pares(n1,n2,n3,n4):
    """Retorna uma tupla contendo apenas os elementos pares da original.
    int,int,int,int->tupla(int)"""
    r=(n1%2,n2%2,n3%2,n4%2)
    if r[0]==0 and r[1]==0 and r[2]==0 and r[3]==0:
        return (n1,n2,n3,n4)
    elif r[0]==0 and r[1]==0 and r[2]==0 and r[3]!=0:
        return (n1,n2,n3)
    elif r[0]==0 and r[1]==0 and r[2]!=0 and r[3]!=0:
        return (n1,n2)
    elif r[0]==0 and r[1]!=0 and r[2]!=0 and r[3]!=0:
        return (n1)
    elif r[0]!=0 and r[1]==0 and r[2]==0 and r[3]==0:
        return (n2,n3,n4)
    elif r[0]!=0 and r[1]!=0 and r[2]==0 and r[3]==0:
        return (n3,n4)
    elif r[0]!=0 and r[1]!=0 and r[2]!=0 and r[3]==0:
        return (n4)
    elif r[0]!=0 and r[1]==0 and r[2]==0 and r[3]!=0:
        return (n2,n3)
    elif r[0]==0 and r[1]!=0 and r[2]!=0 and r[3]==0:
        return (n1,n4)
    elif r[0]==0 and r[1]!=0 and r[2]==0 and r[3]!=0:
        return (n1,n3)
    elif r[0]!=0 and r[1]==0 and r[2]!=0 and r[3]==0:
        return (n2,n4)
    elif r[0]!=0 and r[1]==0 and r[2]!=0 and r[3]!=0:
        return (n2)
    elif r[0]!=0 and r[1]!=0 and r[2]==0 and r[3]!=0:
        return (n3)
    elif r[0]!=0 and r[1]!=0 and r[2]!=0 and r[3]!=0:
        return ()