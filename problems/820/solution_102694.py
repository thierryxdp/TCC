def posLetra(string, letra, n):
    '''Retorna o índice da ocorrência de letra pela nésima vez
    	str, str, int -> int'''
    i = 0
    ocorrencia = 0
    while ocorrencia < n:
    	while i < len(string):
        	if string[i] == letra:
            	ocorrencia = ocorrencia + 1
            else:
        		return -1
        i = i + 1
    return i