def acima_da_media(notas):
    'retorna uma list de nroas em ordem crescente das notas maiores que a media'
    'list---list'

    media = sum(notas)/len(notas)
    if media in notas:
        notas.remove(media)
    return notas