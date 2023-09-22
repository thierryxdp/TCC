def fatorial(n):
    numero=0
    soma=0
    while numero<=n:
        numero=numero+1
        soma=soma+factorial(n)
    return soma