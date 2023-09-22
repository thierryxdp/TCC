def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
    i=0
    while i<len(L):
        if L[i]!= [i]:
            L[i:i]=[i]
            i=i+1
    return L