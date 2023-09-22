def acima_da_media(notas):
    media = []
    for item in notas:
        if item>=3:
            media.append(item)
    media.sort()
    return media