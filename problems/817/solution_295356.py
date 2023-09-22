def acima_da_media(notas):
    newlist = notas
    media = math.ceil(int(sum(newlist)/len(notas)))
    return newlist > media