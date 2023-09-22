def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
    i=0
    resposta=0
    while i<len(L):
        if L[0]!=1:
            L[0:0]=[1]
            return L[0]
        elif L[i]<L[i+1]:
            list.extend(L,[i])
            return L
        i=i+1