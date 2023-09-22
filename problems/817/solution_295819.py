def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    com_zero = quantidade - 1
    media = math.ceil(soma/quantidade)
    if quantidade == 1:
        return []
    media_zero = math.ceil(soma/com_zero)
    if 0 in notas:
        d = list.index(notas, media_zero)
        return notas[d:]
    if media in notas:
        a = list.index (notas, media)
    	return notas[a:] 
    if media not in notas:
        b = media +  1
        c = list.index(notas,b)
        return notas[c:]
    elif media not in notas:
        e = media + 3
        f = list.index(notas, e)
        return notas[f:]