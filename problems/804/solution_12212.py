def filtra_pares(t):
    (n1,n2,n3,n4)=t
    listaA = [n1, n2, n3, n4]
    res = []
    for n in listaA:
        if n%2==0:
            res.append(n)
            return (res)