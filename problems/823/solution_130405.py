def faltante(L):
    """Função que dada uma lista com N-1 inteiros numerados de 1 a N, descubra qual número inteiro
    deste intervalo está faltando """
    i = 0
    L.sort()
    while len(L)>i:
           if L[i] != i+1:
               return i+1
           else:
               i=i+1 
    return i+1