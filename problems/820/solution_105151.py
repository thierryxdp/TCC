def posLetra(s,l,n):
    pos=0 
    valores=[]
	while n!=0:
   		pos=str.find(s,l,pos) 
        n=n-1
    return pos