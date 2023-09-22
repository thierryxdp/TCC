def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo números inteiros
    não repetidos de 1 a N, retorna o numero inteiro x que 
    pertence ao intervalo [1,N] mas que não pertence a lista de
    entrada L. list -> int'''
    t=range(len(L)+1)
    i=0
    while i <len(L):
        if L[i] == t[i]:
        else:
            return L[i]
        i+=1
    return 0