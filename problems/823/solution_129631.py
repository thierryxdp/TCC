def faltante(L):
    """dada uma lista L de tamanho N-1 contendo números inteiros (não repetidos) de 1 a N, a função retorna o número 
    inteiro x que pertence ao intervalo [1,N] mas que não pertence a lista de entrada L; list -> int"""
    list.sort(L)
    
    i = 0
    j = 1
    while i < len(L):
        if L[i] != j:
            return j
        i = i + 1
        j = j + 1
        
    return j