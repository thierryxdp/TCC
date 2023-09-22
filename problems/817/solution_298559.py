import math
def acima_da_media(notas):
    notasn = notas[:]
    media = sum(notas)/len(notasn)
    media = math.ceil(media)
    notasn.insert(media)
    notasn.sort()
    posicao = notasn.index(media) + 1
    notas_finais = notasn[posicao:]
    return notas_finais