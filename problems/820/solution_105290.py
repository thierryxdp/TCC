def posLetra(s,l,n):
	pos=-1 
	while n!=0:
		n=n-1
		pos=str.find(s,l,pos+1)
	return pos