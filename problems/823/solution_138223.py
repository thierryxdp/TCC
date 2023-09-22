def faltante(lista):
    ''' Essa função recebe uma lista conendo números inteiros, e retorna o número que falta na sequência da lista;
    list -> int. '''
    f = len(lista)+1
    N = 1
    i = 0
    while i <= f:
        if N == f:
            return N
        elif N != lista[i]:
            return N
        N = N+1
        i = i+1