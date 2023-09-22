def faltante(L):
    """Funcao que dada uma lista N - 1 inteiros numerados de 1 a N,
    retorna o numero inteiro que esta faltando deste intervalo;
    list -> int"""
    
    n = len(L) + 1
    somatorioL = sum(L)
    listaN = list(range(1,n+1))
    somatorioN = sum(listaN)

    return somatorioN - somatorioL