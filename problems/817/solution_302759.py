def acima_da_media(x):
    r = 0
    for y in x:
        if y>0:
            r = r + y
	media = r/len(x)
	media = media - 0.1
	x.append(media)
    return x
    x.sort()
	return x[x.index(media)+1:]