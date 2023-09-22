def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    a = list.index (notas, media)
    b = a+1
    c = media +1
    if media in notas:
    	return notas[a:]
    if media not in notas:
        a = list.index(notas,c)
        return notas[b:]