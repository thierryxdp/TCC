import math
def acima_da_media(notas):
    notas_vazia = []
    notas1 = notas[:]
    notas2 = notas[:]
    notas3 = notas[:]
    zero = notas2.count(0)
    media = sum(notas1)/(len(notas2) - zero)
    media = math.ceil(media)
    notas1.append(media)
    notas1.sort()
    posicao = notas1.index(media)
    notas_finais = notas1[posicao:]
    notas_finais.remove(media)
    if len(notas) == 1:
        return notas_vazia
    else:
        return notas_finais