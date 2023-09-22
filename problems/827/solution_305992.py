def qtd_divisores(n):
    listaA=[]
    
    for numero in range(1,n+1):
        if numero%n==0:
            listaA.append(n)
    return len(listaA)