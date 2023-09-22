def qtd_divisores(n):
    listaA=[]
    numero=n
    for numero in range(numero//2+1):
        if numero%numero==0:
            listaA.append(numero)
    return len(listaA)