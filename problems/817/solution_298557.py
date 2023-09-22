def acima_da_media(notas):
    notasn = notas[:]
    media = sum(notas)/len(notas)
    media = round(media)
    notasn.sort()
    posicao = notasn.index(media)
    notas_finais = notasn[posicao:]
    return notas_finais