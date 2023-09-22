def posLetra(s,l,n):
    s=[s]
    pos=0 
	while l in s:
   		pos=str.find(s,l,pos)
        s=s[pos+1:]     	
    return pos