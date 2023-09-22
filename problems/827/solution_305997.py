def qtd_divisores(n):
    listaA=[]
    numero=0
    for numero in range(1,n+1):
        if n%n==0:
            listaA.append(numero)
    return len(listaA)