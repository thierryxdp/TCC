def posLetra(s,l,n):
    '''recebe uma string(s), uma letra(l), e um número(n) que indica a ocorrência
    desejada da letra, e retorna em que posição da string aquela ocorrência da letra está;
    str, str, int -> int'''
    a = 0
    contador = 0
    f = list(s)
    while contador < n:
        if l in f:
        	a = f.index(l)
        else:
            return -1
		f[a] = '#'
        contador = contador + 1
    return a