def faltante(pecas):
    N=len(pecas)+1
    #pecas.sort()
    x=1
    while(x<=N):
    	if(x not in pecas):
    		return x
    	x+=1