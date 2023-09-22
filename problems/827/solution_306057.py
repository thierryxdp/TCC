def qtd_divisores(n):
    """Conta quantos divisores um número tem;int->int"""
    contador=0
    for i in range(n+1):
        if n%i==0:
            contador=contador+1
    return contador