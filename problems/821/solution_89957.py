def fatorial(n):
    '''recebe um numero inteiro e retorna o fatorial do mesmo
    entrada: int
    saida: int'''
    proximo=1
    fatorial=1
    while proximo <= n:
        fatorial=proximo*fatorial
        proximo = proximo + 1
    return fatorial