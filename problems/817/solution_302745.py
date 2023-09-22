def acima_da_media(x):
    r = 0
    for y in x:
        if y>0:
            r = r + y
		media = r/len(x)
        media = media - 1/10
        return media
	x.append(media)
    x.sort()
	x[x.index(media)+1:]