def posLetra(s,letra,n):
    l=list(s)
    indices=[]
    x=0
    while x<len(l):
        if l[x]==letra:
            indices.append(x)
		x+=1
	if n>len(indices):
        return -1
    else:
        return indices[n-1]