def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
    i=0
    um=l[0]
    n=l[-1]
    while i>len(L):
        if L[i]!=i:
            L[i:i]=i
        	i=i+1
    return L