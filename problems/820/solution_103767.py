def posLetra(frase, letra, n):
    '''retorna a posição da string em que há a ocorrência de uma letra dada em uma frase
    str, str, int -> int'''
	i = 0
    ocorrencia = 0
    while i < len(frase):
        if frase[i] == letra:
            if ocorrencia == n:
                return i
            else:
                ocorrencia = ocorrencia + 1
		i = i + 1
	return -1