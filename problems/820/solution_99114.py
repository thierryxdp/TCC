def posLetra(texto, letra, ocorrencia):
    i=0
    o=0
    ind=i
    while i<len(texto) and not(0==ocorrencia):
        if texto[i]!='a':
            i=1+i
        if texto[i]=='a':
            o=o+1
            ind=i
            i=i+1
	if o<ocorrencia:
        return -1
    return ind