def media(notas):
    return sum(notas)/len(notas)

def acima_da_media(notas):
    if len(notas)==1:
        return []
    if media(notas) in notas:
        notas.sort()
        return notas[notas.index(media(notas))+1:len(notas)]
    else:
        notas.append(media(notas))
        notas.sort()
        return notas[notas.index(media(notas))+1:len(notas)]