def faltante(pecas):
    N=max(pecas, key=int)
    x=0
    while(x<=N):
    	x+=1
    	if(x in pecas):
    		return x