def posLetra(s,l,n):
	pos=-1 
	r=str.count(s,l)
	while n!=0:
		n=n-1
		pos=str.find(s,l,pos+1)
	return pos