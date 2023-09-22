def posLetra(s,l,n):
    pos=-1
	while l in s:
    	pos=str.find(s,l)
        s=s[pos+1:]
    return pos