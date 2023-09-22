def acima_da_media(x):
    r = 0
    for y in x:
        if y>0:
            r = r + y
		media = r/len(x)
	x.append(media)
    x.sort()
    list.split(x, media)
    return x