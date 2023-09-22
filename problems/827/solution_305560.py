def qtd_divisores(n):
    listaA=[]
    for i in range(1,n+1):
        if numero%i==0:
            listaA.append(numero)
    return len(listaA)