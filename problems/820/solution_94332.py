def posLetra(string,letra,n):
    ''' Retorna a posição da string aquela ocorrencia da letra está'''
    i = 0
    while i < n:
    	if string[i] == letra:
        	i = i + 1
    	return i
    else:
        return -1