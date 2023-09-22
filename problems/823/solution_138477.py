def faltante(pecas):
    '''Função que retorna a quantidade de peças que estão faltando
    uma vez dada a lista, pecas, com N-1 contendo números inteiros 
    e o intervalo [1, N]
    list=>int'''
    i=1
    N_falta=[]
    while i <= len(pecas):
        if i not in pecas:
            N_falta += 1
        i = pecas[i]+1
    if N_falta == 0:
            N_falta += len(pecas)+1
    return N_falta