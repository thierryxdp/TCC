def maiores(l, n):
    '''Retorna uma lista com os númeors maiores que n.
    list, int -> list'''
    list.append(l, n)
    list.sort(l)
    i = list.index(l, n) + 1
    if list.count(l, n) > 0:
        maiores(l[i:], n)
    return l[i:]

def acima_da_media(l):
    '''Retorna as notas que ficaram acima da média.
    list -> list'''
    media = sum(l) / len(l)
    return maiores(l, media)