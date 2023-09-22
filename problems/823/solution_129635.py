def peca_perdida(pecas):
    '''Função que, dada uma lista com todas as pessas que a criança possúi, retorna a peca que está faltando.
    list --> int'''
    list.sort(pecas)
    i = 0
    cheia = list(range(1,len(pecas)+2))
    while pecas[i] == cheia[i]:
        i = i + 1
    return cheia[i]