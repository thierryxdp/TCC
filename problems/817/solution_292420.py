def acima_da_media(Notas):
    from math import ceil
    media = math.ceil(sum(Notas)//len(Notas))
    if media in Notas:
        list.sort(Notas)
        return Notas[media+1:]
    if media not in Notas: