def acima_da_media(Notas):
    media = int(sum(Notas)/len(Notas))
    if media in Notas:
        list.sort(Notas)
        return Notas[media:]
    if media not in Notas:
        list.append(Notas, media)
        return Notas[media+1:]