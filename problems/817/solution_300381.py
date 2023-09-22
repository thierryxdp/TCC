def acima_da_media(notas):
    media= sum(notas) / len(notas)
    if media in notas:
        list.sort(notas)
        lista_notas = [list.index(notas, media)+1:]
        return lista_notas
    else:
        notas.insert(-1,media)