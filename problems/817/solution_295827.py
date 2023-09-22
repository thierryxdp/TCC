def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    a = list.index(notas, media)
    b = a+1
    if media in notas:
    	return notas[b:] 
    if media not in notas:
        c = b +1
        return notas[c:]