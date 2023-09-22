def maiores(l, n):
    '''Retorna uma lista com os números maiores que n.
    list, int -> list'''
    list.append(l, n)
    list.sort(l)
    i = list.index(l, n) + 1
    return l[i:]

def acima_da_media(l):
    '''Retorna as notas que ficaram acima da média.
    list -> list'''
    media = sum(l) / len(l)
    maioresAVG = maiores(l, media)
    print(list.count(maioresAVG, media) > 0, maiores(maioresAVG, media), maioresAVG)
    if list.count(maioresAVG, media) > 0:
    	return maiores(maioresAVG, media)
    return maioresAVG