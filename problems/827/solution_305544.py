def qtd_divisores(n):
    listaA=[]
    i=0
    for i in range(1,n+1):
        if i%i==0:
            listaA.append(i)
    return len(listaA)