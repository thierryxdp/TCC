def faltante(pecas):
	list.sort(pecas)
	i=1
    if pecas[0]!=1:
        return 1
    while i<len(pecas):
        if pecas[i]==pecas[i+1]+1:
            i+=1
            return pecas[len(pecas)-1]+1
        if pecas[i]==pecas[i+1]-1:
            i+=1
            return pecas[i]+1