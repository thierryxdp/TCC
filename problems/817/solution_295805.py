def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    com_zero = quantidade - 1
    media = math.ceil(soma/quantidade)
    media_zero = math.ceil(soma/com_zero)
    if 0 in notas:
        j = list.index(notas, media_zero)
        return notas[j:]
    if media in nota:
        a = list.index (notas, media)
    	return notas[a:] 
    elif media in notas:
        b = list.index(notas, media)
        c = b + 1
        return notas[b:]