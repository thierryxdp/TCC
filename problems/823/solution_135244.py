def faltante(pecas):
	list.sort(pecas)
	i=1
    if pecas[0]!=1:
            return 1
    while i<len(pecas):
        if pecas[i]==pecas[i+1]+1:
            i+=1
    return i+1
    else:
        return pecas[len(pecas)-1]+1