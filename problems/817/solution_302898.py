def acima_da_media(notas):
    """Função que recebe uma lista com as notas de alunos,
    calcula a media cria uma ordenada com as notas que ficaram
    acima da media
    list->list"""
    notas_media =[]
    media = sum(notas)/len(notas)
    for i in range (len(notas)):
        if notas[i] > media:
            notas_media.append(notas[i])
            notas_media.sort()
            return notas_media