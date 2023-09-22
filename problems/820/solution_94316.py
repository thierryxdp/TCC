def posLetra(s,l,n):
    """ dada uma string 's' retorna a posição que a letra 'l' está na ocorrência
    'n' desejada; caso haja menos ocorrências da letra do que foi pedido, a função
    retorna -1.
    str, str, int -> int """
    string = s
    posicao = []
    i = 0
    if str.count(string,l) < n:
        return -1
    while i<=len(s):
        if string[i] == l:
            posicao += [i]
        i = i+1
    return posicao[-1]