def acima_da_media(notas):
    'retorna uma list de nroas em ordem crescente das notas maiores que a media'
    'list---list'
    maiores=()
    media = sum(notas)/len(notas)
    if media in notas:
        notas.remove(media)
    return maiores.tuple(notas,media)