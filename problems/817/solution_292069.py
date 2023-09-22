def acima_da_media(notas):
    media = []
    for item in notas:
        if item>5:
            media.append(item)
    media.sort()
    return media