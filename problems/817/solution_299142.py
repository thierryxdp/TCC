def acima_da_media (x):
    z=len(x)
    q=sum(x)
    m=q/z
	x.append(m)
    list.sort(x)
    y =x.index (m) + 1
    return x[y:]