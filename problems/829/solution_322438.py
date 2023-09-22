def soma_h(n):
    """Dado o índice numérico n, retorna a soma de uma função H(1+1/2+1/N),
    n vezes:
    int-->int"""
    soma=0
    for numero in range(1,n+1):
        soma+=1/numero
    return round(soma,2)