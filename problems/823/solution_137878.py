def faltante(L):
	'''
    Recebe uma lista L de inteiros de tamanho N-1 e retorna o inteiro no
    intervalo [1,N] que não está na lista
    
    list -> int
    '''
    x=1
    while x in L:
        x=x+1
    return x