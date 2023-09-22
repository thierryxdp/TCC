def qtd_divisores(n):
    """essa funcao calcula e retorna quantos divisores um numero tem; int-> int"""
    listaA=[]
    numero=n
    for i in range(1,n+1):
        if numero%i==0:
            listaA.append(i)
    return len(listaA)