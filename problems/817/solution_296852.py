def acima_da_media (notas: list)->list:
    ''''''
    media= sum(notas)/len(notas)
	copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicao= copianotas.index(notas)
    maiores= copianotas[posicao + 1:]
    if n in maiores:
        quant= maiores.count(n)
        maiores = maiores[quant:]
    return maiores