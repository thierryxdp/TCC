def qtd_divisores(n):
    listaA=[]
    for numero in range(1,n+1):
        numero=n
        if numero%numero==0:
            listaA.append(numero)
            return len(listaA)