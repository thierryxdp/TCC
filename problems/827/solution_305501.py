def qtd_divisores(n):
    listaA=[]
    for numero in range(1,n+1):
        numero=n
        for i in range (1,0,-1):
            numero%numero==0
            listaA.append(numero)
            return numero