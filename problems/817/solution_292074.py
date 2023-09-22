def acima_da_media(notas):
    media = []
    media1= sum(notas)/len(notas)
    for item in notas:
        if item>=media1:
            media.append(item)
    media.sort()
    return media