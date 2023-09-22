def qtd_divisores(n):
    """funçao que conta quantos divisores o numero tem. int->int"""
    a=range(n+1)
    indice=1
    soma=0
    for numero in range(1,n+1):
        if n % a[indice]==0:
        soma= soma+indice
        indice=indice+1
    return soma