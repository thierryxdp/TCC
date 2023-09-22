def acima_da_media(notas):
    newlist = notas
    media = int(sum(newlist)/len(notas))
    return newlist > media