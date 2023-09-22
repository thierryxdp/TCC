def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    if media in notas:
        a = list.index (notas, media)
    	return notas[a:]
	if media not in notas:
        b = media + 1
        c = list.index(notas, b)
        return notas[a:]