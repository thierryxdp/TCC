def posLetra(s,l,n):
    s=[s]
    pos=-1 
	while l in s:
    	if n!=-1:
        	pos=str.find(s,l)
        	s=[s[pos+1:]]+s  	
    return pos[n]