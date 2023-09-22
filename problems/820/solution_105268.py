def posLetra(s,l,n):
	pos=-1 
	r=str.count(s,l)
	while r>=n:
		r=r-1
		pos=str.find(s,l,pos+1)
    if n==1:
        return str.index(s,l)
	return pos