def acima_da_media(notas: list[float]) -> list[float]:
    '''Retorna as notas que estão acima da média'''
    media = sum(notas)/len(notas)
    copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicao= copianotas.index(media)
    maiores= copianotas[posicao + 1:]
    if media in maiores:
        quant= maiores.count(media)
        maiores= maiores[quanr :]
        return maiores