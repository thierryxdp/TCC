def faltante(pecas):

    list.sort(pecas)

    i = 0

    while i < len(pecas)-1:
        if (pecas[i] - pecas[i+1]) != -1:
            return pecas[i]+1
		i = i + 1
        
    if len(pecas) == 1 and pecas[0] != 1:
        return pecas[0]-1
    
    return pecas[len(pecas)-1] + 1