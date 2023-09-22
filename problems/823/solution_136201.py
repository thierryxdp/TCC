def faltante (pecas):
    '''Retorna a peca faltante dos numeros dados, ou
    seja, o numero que falta na sequencia da lista dada
    list --> int'''
    list.sort(pecas)
    i = 0
    if pecas[0]==2:
        return 1
    while i < len(pecas):
        if pecas[i+1] != pecas [i]+1:
            return pecas [i]+1
        else:
            i = i+1
    return pecas[len(pecas)-1]+1