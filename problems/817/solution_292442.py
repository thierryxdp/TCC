def acima_da_media(Notas):
    import math
    from math import ceil
    media = round(sum(Notas)/len(Notas))
    if media in Notas:
        list.sort(Notas)
        return Notas[media]
    else:
        Nota2 = list.append(Notas, media)
        list.sort(Notas)
        return Notas[media]