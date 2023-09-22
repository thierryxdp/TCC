def acima_da_media(Notas):
    import math
    from math import ceil
    media = math.ceil(sum(Notas)//len(Notas))
    if media in Notas:
        list.sort(Notas)
        return Notas[media+1::1]
    if media not in Notas:
        Nota2 = list.append(Notas, media)
        list.sort(Notas)
        return Notas[media+1::1]