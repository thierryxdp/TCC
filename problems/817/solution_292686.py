def acima_da_media(Notas):
    import math
    from math import floor
    media = floor(sum(Notas)/len(Notas))
    if media in Notas:
        list.sort(Notas)
        Local = list.index(Notas, media)
        return Notas[Local+1:]
    elif media not in Notas:
        list.append(Notas, media)
        list.sort(Notas)
        Local = list.index(Notas, media)
        return Notas[Local+1:]