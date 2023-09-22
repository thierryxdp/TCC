def qtd_divisores(num):
    listaA=[]
    numero=n
    for i in range(1,n+1):
        if numero%i==0:
            listaA.append(i)
    return len(listaA)