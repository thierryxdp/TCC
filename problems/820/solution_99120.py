def posLetra(texto, letra, ocorrencia):
    i=0
    o=0
    ind=[]    
    while not(o==ocorrencia):
        if texto[i]==letra:
            o=o+1
            ind=i
        i=i+1
    if o<ocorrencia:
        return -1
    else: 
    	return list.pop(ind, -1)