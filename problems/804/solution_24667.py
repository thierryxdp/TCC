def filtra_pares(tupla):
    """ygdwgdwjgw"""
    n1,n2,n3,n4 = tupla
    A == n1//2 
    B == n2//2 
    C == n3//2 
    D == n4//2 
    if (A and B and C and D )==0:
        return(n1,n2,n3,n4)
    elif (A and B and C)==0:
        return(n1,n2,n3)
    elif (A and B)==0:
        return(n1,n2)
    elif (A)==0:
        return(n1)
    elif (B)==0:
        return(n2)
    elif(C)==0:
        return(n3)
    elif(D)==0:
        return(n4)
    elif(B and C)==0:
        return(n2,n3)
    elif(B and D)==0:
        return(n2,n4)
    elif(C and D)==0:
        return(n3,n4)
    elif(B and C and D)==0:
        return(n2,n3,n4)
    else:
        return('')