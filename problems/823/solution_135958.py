def faltante(L):
    """dada uma lista L contendo numeros de 1 a N, retorna o numero inteiro que falta no intervalo passado;
    list -> int"""
    N=len(L)+1
    n=N*(1+N)/2-sum(L)
    return n