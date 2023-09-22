def posLetra(string, letra, num):
    '''Funcao que retorna a posicao da ocorrencia na string'''
    ''' str, str, int -> int'''
    for i in range(len(string)):
		if string [i] == letra:
			ocorrencia = i
        if ocorrencia < numero:
            ocorrencia = -1
	return ocorrencia