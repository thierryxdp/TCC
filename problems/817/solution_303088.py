def acima_da_media(notas):
    """Essa função recebe uma lista com as notas de alunos, calcula a media cria uma ordenada com as notas que ficaram acima da media
    list -> list"""
    notas_media =[]
    media = sum(notas)/len(notas)
    for x in range (len(notas)):
        if notas[x] > media:
            notas_media.append(notas[x])
    notas_media.sort()
    return notas_media