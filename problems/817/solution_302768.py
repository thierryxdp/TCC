def acima_da_media(x):
    if x[0] == x[0]/len(x):
        return "a"
    r = 0
    for y in x:
        if y>0:
            r = r + y
	media = r/len(x)
	x.append(media)
    x.sort()
	return x[x.index(media)+1:]