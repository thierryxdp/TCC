def acima_da_media(x):
    """A função calcula a media das notas e filtra as que estão abaixo da media e retorna uma lista com as acima da media
    list --> list"""
    if x[0] == x[0]/len(x):
        return []
    r = 0
    for y in x:
        if y>0:
            r = r + y
	media = r/len(x)
	x.append(media)
    x.sort()
	return x[x.index(media)+1:]