def posLetra(texto, letra, ocorrencia):
    '''Função que indica a posição da letra numa determinada ocorrencia desejada. list, str, int ->int '''
    i=0
    o=0
    ind=[]    
    while i<len(texto) and not(o==ocorrencia):
        if texto[i]==letra:
            o=o+1
            ind=i
        i=i+1
    if o<ocorrencia:
        return -1
    else: 
    	return ind