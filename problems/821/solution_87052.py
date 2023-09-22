def fatorial(n):
    n=n if n>1 else 1
    indice=1
    for contador in range(1,n+1):
        indice= indice*contador
    return indice