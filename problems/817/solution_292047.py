def acima_da_media(notas):
    """Função que dada uma lista de números inteiros nos retorna aqueles que são maiores que a média dos números. 
    list -> list """

    media = int((sum(notas)/len(notas)))

    list.append(notas, media)
    list.sort(notas)

    if notas[list.count(notas, media)] != 1 and notas[list.count(notas, media)] != 0:
        return notas[(list.index(notas, media)+2):]

    else:
        return notas[(list.index(notas, media)+1):]