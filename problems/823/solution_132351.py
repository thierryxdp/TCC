def faltante(L):
    '''Dado uma lista L de tamanho N-1 contendo numeros inteiros de 1 a N
    list -> int'''
	i=1
    while i<len(L):
        if L[i]==L[i-1]+2:
            L[i:i]=[i+1]
        i=i+1
    return L[i:i]