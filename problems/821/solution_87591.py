def fatorial(numero):
    '''Função que, dado um número, calcula seu fatorial.
    	int -> int'''
    fatorial=1
    i=1
    while i<=numero:
        fatorial=fatorial*i
        i=i+1
    return fatorial