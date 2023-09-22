def filtra_pares(t):
    n1,n2,n3,n4=t
    par(n1%2==0, n2%2==0, n3%2==0, n4%2==0)
    impar(n1%2!=0, n2%2!=0, n3%2!=0, n4%2!=0)
    return par()