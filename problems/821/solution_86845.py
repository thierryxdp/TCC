def fatorial(n):
    numero=0
    soma=0
    while numero<=n:
        numero=numero+1
        soma=soma+fatorial(n)
    return soma