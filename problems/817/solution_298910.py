import math
def acima_da_media(notas):
    notasn = notas[:]
    media = sum(notas)/len(notasn)
    media = math.ceil(media)
    notasn.append(media)
    notasn.sort()
    posicao = notasn.index(media)
    notas_finais = notasn[posicao:]
    notas_finais.remove(media)
    return notas_finais