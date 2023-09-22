def acima_da_media(notas: list)->list:
    "Dada uma lista com as notas, retorna aquelas que ficaram acima da media"
    media= sum(notas)/len(notas)
    copianotas= notas.copy()
    copianotas.append(media)
    copianotas.sort()
    posicao= copianotas.index(media)
    maiores=copianotas [posicao + 1:]
    if media in maiores:
        quant = maiores.count(media)
        maiores = maiores[quant:]
    return maiores