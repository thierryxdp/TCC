def posLetra(frase,letra,ocorrencia):
    i=0
    o=0
    while i<len(frase) and o<ocorrencia:
    	if frase[i]==letra:
            o=o+1
            pos=i
   			i=i+1
	if o==ocorrencia:
        return -1
    else:
        return pos