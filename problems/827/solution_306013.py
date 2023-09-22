def qtd_divisores(n):
    listaA=[]
    
    for numero in list(range(1,n+1)):
        if n%numero ==0:
            listaA.append(numero)
    return len(listaA)