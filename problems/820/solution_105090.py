def posLetra(s,l,n):
    pos=-1
    s=[]
	while l in s:
    	pos=str.find(s,l)
        s=[s[pos+1:]]+s
    return s[n-1]