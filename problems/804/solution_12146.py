def filtra_pares(t):
    n1,n2,n3,n4=t
    list((n1,n2,n3,n4)%2!=0)
    filter((n1,n2,n3,n4)%2==0)
    return filter()