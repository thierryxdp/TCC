def faltante(L):
    '''Dada uma lista L de N-1 números inteiros de 1 a N, retorna o número faltante nesse intervalo
    entrada: lista
    saída: int
    '''
    list.sort(L)
    N=L[-1]
    somaateN=N
    while N>0:
        N=N-1
        somaateN=somaateN+N
    somalista=sum(L)
    if somaateN==somalista:
        return L[-1]+1
    else:
        x=somaateN-somalista
    	return x