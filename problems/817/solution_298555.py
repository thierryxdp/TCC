def acima_da_media(notas):
    notas.append(5)
    notasn = notas[:]
    notasn.sort()
    posicao = notasn.index(5) + 1
    notas_finais = notasn[posicao:]
    return notas_finais