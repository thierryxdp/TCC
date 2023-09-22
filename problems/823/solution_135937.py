def faltante(L):
    """dada uma lista L contendo numeros de 1 a N, retorna o numero inteiro que falta no intervalo passado;
    list -> int"""
    i=1
    n=1
    N=len(L)+1
    
    while i<len(L):
        if i!=L[i-1]:
            return i