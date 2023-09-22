def acima_da_media(notas):
    media=sum(notas)/len(notas)
    acima_da_media=[]
    for c in notas:
        if c>=media:
            acima_da_media.append(c)
    return acima_da_media