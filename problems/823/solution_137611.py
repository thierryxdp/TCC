def faltante(L):
    '''
	função que recebe uma lista L de tamanho N - 1 contendo números inteiros não repetidos de 1 a N e retorna um número inteiro x que pertence ao intervalo [1,N], mas que não pertence a lista de entrada L;
    list -> int
    '''
	list.sort(L)
    i = -1
    final = len(L) + 1
    while abs(i) < len(L):
        if L[i] == final:
            final = final - 1
        i = i - 1
    if L[i] != final:
        return final