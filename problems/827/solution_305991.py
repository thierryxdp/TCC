def qtd_divisores(n):
    listaA=[]
    
    for numero in range(1,n+1):
        if n%n==0:
            listaA.append(n)
    return len(listaA)