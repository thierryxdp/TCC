def acima_da_media(notas):
    """Função que dada uma lista de números inteiros retorna os números que estão acima da média.
    list -> list """

    media = (sum(notas)/len(notas))

    list.append(notas, media)
    list.sort(notas)


    return notas[list.index(notas, int(media)+1):]