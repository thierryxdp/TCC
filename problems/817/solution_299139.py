def acima_da_media (x):
    w=len(x)
	x.append(w)
    list.sort(x)
    y =x.index (w) + 1
    return x[y:]