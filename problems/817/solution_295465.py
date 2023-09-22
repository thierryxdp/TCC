def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    b = a+1
    c = media +1
    d = list.index(notas,c)
    if media in notas:
        a = list.index (notas, media)
    	return notas[a:]