def filtra_pares(t):
    n1,n2,n3,n4 =t 
    if n1%2==0 and n2%2==0 and n3%2==0 and n4%2==0 or (n1,n2,n3,n4)%2!=0:
        return (n1,n2,n3,n4)
    else:
        return ()