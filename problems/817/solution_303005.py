def acima_media(notas):

    """Retorne uma lista de notas crescente com todas notas maiores que a media;

    list - > list"""

    media = sum(notas)/len(notas)

    if media in notas:

        notas.remove(media)

    return maiores(notas,media)