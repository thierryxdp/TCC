def faltante(pecas):
    '''Função que, dada uma lista com todas as pessas que a criança possúi, retorna a peca que está faltando.
    list --> int'''
    list.sort(pecas)
    i = 0
    cheia = list(range(1,len(pecas)+2))
    cheia2 = list(range(1,len(pecas)+1))
    if pecas == cheia2:
        return pecas[len(pecas)-1] + 1
    else:
        while pecas[i] == cheia[i]:
            i = i + 1
        return cheia[i]