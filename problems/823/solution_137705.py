def faltante(l: list):
    ''' função que dada uma lista com números inteiros,
    reotrne qual número inteiro falta na lista. list-str'''
    posicao = 0
    while l[posicao] < len(l):
        if posicao+1 == l[posicao]:
            posicao = posicao + 1
        break
    return posicao+1