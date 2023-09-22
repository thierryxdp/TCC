def qtd_divisores(n):
    listaA=[]
    numero=n
    for numero in range(1,n+1):
        if numero%numero==0:
            listaA.append(numero)
    return listaA