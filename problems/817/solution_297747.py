def maiores(l, n):
    '''Retorna uma lista com os números maiores que n.
    list, int -> list'''
    list.append(l, n)
    list.sort(l)
    i = list.index(l, n) + list.count(l, n)
    return l[i:]

def acima_da_media(l):
    '''Retorna as notas que ficaram acima da média.
    list -> list'''
    if len(l) < 2:
        return []
    media = sum(l) / len(l)
    return maiores(l, media)