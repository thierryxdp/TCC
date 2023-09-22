def soma_h(n):
    """entrada é um numero inteiro e na saída é um float!"""
    soma = 0
    for numero in range(1,n+1):
        soma+=(1/numero)
    return round(soma,2)