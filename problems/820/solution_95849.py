def posLetra(string, letra, numero):
	i = 0
	while i < len(string):
		if string[i] == letra:
			ocorrencia = i
        if ocorrencia < numero:
            ocorrencia = -1
		i = i + 1
	return ocorrencia