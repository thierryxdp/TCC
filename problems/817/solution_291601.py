def acima_da_media(notas):
    media = sum(notas)/len(notas)
    list.append(notas,media)
    list.sort(notas)
    a = list.index(notas,media)
    if media in notas:
        return notas[a+2:]
    else:
    	return notas[a+1:]