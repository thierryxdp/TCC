def acima_da_media(notas,n):
    media = []
    for item in notas:
        if item>=n:
            media.append(item)
    media.sort()
    return media