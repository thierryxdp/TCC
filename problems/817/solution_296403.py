def acima_da_media(notas):
    """ Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media 
    list -> list """
    media = sum(notas)/len(notas)
    print(f'media: {media}')
    notas.append(media)
    notas.sort()
    notas = notas[notas.index(media)+1:]
    return notas