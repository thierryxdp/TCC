def acima_da_media(notas: list[float]):
    media = sum(notas)/len(notas) 
    notas.append(media)
    notas.sort()
    if media == notas[-7]:
        return [notas[-6],notas[-5],notas[-4],notas[-3],notas[-2],notas[-1]]
    elif notas[-6] == media:
        return [notas[-5],notas[-4],notas[-3],notas[-2],notas[-1]]
    elif notas[-5] == media:
        return [notas[-4],notas[-3],notas[-2],notas[-1]]
    elif notas[-4] == media:
        return [notas[-3],notas[-2],notas[-1]]
    elif notas[-3] == media:
        return [notas[-2],notas[-1]]
    elif notas[-2] == media:
        return [notas[-1]]
    else:
        return []