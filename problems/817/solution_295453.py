def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    if media in notas:
        a = list.index (notas, media)
        b = a+1
    	return notas[a:]
    if media not in notas:
        c = media +1
        d = list.index(notas,c)
        return notas[b:]