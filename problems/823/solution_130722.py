def faltante(L):
    '''Função que dada uma lista de tamanho N-1 com números inteiros
    de 1 a N, retorna o número que está faltando na sequência
    list -> int'''
    i = 0
    L.sort()
    while i < len(L):
        if L[i] != i + 1:
            return i + 1
        elif L[i] == L[-1]:
            return L[i] + 1
        else:
            i = i + 1