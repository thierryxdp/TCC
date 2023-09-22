def acima_da_media(notas):
    import math
    list.sort(notas)
    soma = sum(notas)
    quantidade = len(notas)
    media = math.ceil(soma/quantidade)
    if media in notas:
        a = list.index (notas, media)
        b = a - 1
    	return notas[b:]