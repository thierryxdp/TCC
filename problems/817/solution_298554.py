def acima_da_media(notas):
    notas.append(6)
    notasn = notas[:]
    notasn.sort()
    posicao = notasn.index(6) + 1
    notas_finais = notasn[posicao:]
    return notas_finais