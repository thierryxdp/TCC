def posLetra(s,l,n):
    pos=0 
    valores=[]
	while len(valores)== n:
   		pos=[str.find(s,l,pos)]
        valores=[pos]+pos
        n=pos+1
          	
    return pos