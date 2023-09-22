def posLetra(s,l,n):
    pos=0 
	while list.count(pos)!= n:
   		pos=[str.find(s,l,pos)]
        n=pos+1
          	
    return pos