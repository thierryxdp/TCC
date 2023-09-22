def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
    i=0
    resposta=0
    while i+1<len(L):
        if L[i+1]!=i+1:
            L[i+1:i+1]=[i]
        i=i+1
    return L