def acima_da_media(Notas):
    media = (sum(Notas)//len(Notas))
    if media in Notas:
        list.sort(Notas)
        return Notas[media+1:]
    if media not in Notas:
        list.append(Notas, media)
        list.sort(Notas)
        ListaAtualizada = list.remove(Notas, media)
        return ListaAtualizada[media+1:]