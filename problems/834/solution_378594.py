def media_matriz(m):
    s=0
    c=0
    for x in m:
        for y in x:
            c+=1
            s+=y
	return round(s/c,2)