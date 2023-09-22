def fatorial(n):
    ''''função que, dado um número retorna o fatorial dele.
    int -> int'''
    i=1
    fatorado=1
    
    while i<=n:
        fatorado=fatorado*i
        i=i+1
    return fatorado