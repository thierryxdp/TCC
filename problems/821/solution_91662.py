def fatorial(n):
    'função que recebe um número e calcula seu fatorial. int->int'
    resultado=1
    while n>0:
        resultado=resultado*(n-1)
    n-=1
    return resultado