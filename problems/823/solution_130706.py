def faltante(L):
    '''Função que dada uma lista de tamanho N-1 com números inteiros
    de 1 a N, retorna o número que está faltando na sequência
    list -> int'''
    i = 0
    while (L[i+1] == L[i] + 1 or L[i+1] == L[i] - 1) and i < len(L):
        i = i + 1
    if L[i] > L[i-1]:
        return L[i-1] + 1
    if L[i] < L[i-1]:
        return L[i-1] - 1