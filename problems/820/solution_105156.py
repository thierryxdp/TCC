def posLetra(s,l,n):
    pos=0 
    n=s
	while s>=0:
   		pos=str.find(s,l,pos) 
        s=s-1
    return pos