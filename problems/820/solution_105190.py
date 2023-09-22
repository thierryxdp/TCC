def posLetra(s,l,n):
    pos=-1 
    r=str.count("banana","a")
	while r>=n:
   		r-1
        pos=str.find(s,l,pos+1)       
    return pos