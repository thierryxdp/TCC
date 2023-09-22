def acima_da_media(Notas):
    media = (sum(Notas)//len(Notas))
    if media in Notas:
        list.sort(Notas)
        return media
    if media not in Notas:
        list.append(Notas, media)
        return media