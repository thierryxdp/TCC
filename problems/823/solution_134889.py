def faltante(pecas):
	list.sort(pecas)
	i=0
	if pecas[0]!=1:
        return 1
    while pecas[i]==pecas[i+1]-1:
		i+=1
	    return pecas[i]+1
    else:
        return pecas[len(pecas)]+1