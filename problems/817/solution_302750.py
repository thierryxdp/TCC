def acima_da_media(x):
    r = 0
    for y in x:
        if y>0:
            r = r + y
            return r
		media = r/len(x)
        media
	x.append(media)
    x.sort()
	x[x.index(media)+1:]