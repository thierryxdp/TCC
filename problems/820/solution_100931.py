def  posLetra(frase,letra,ocorrencia):
    i = 0
    nocs = 0
    	while <len(frase) and nocs < ocorrencia:
        if frase[i] == letra:
            nocs = nocs + 1
        i = i + 1
    if nocs < ocorrencia:
        return -1 
    else:
        return i-1