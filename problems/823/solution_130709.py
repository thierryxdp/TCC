def faltante(L):
    '''Função que dada uma lista de tamanho N-1 com números inteiros
    de 1 a N, retorna o número que está faltando na sequência
    list -> int'''
    N = len(L) + 1
    i = 0
    while i != N - 1:
        if L[i+1] > L[i] + 1:
            x = L[i] - 1
        if L[i+1] < L[i] - 1:
            x = L[i] + 1
        if L[i] == L[-1]:
            x = L[i] + 1
        if len(L) == 1:
            return L[0] + 1
    i = i + 1 
    return x