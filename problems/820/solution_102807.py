def posLetra(frase, letra, n):
	''' função retorna posição da letra na ocorrência (n)
	str, str, int --> int'''
	texto = list(frase)
	ctd = 0
	ocorrencia = 0
	while len(texto) > ctd:
		if letra in texto[ctd]:
			ocorrencia += 1
			if ocorrencia == n:
				return ctd
		ctd += 1
	if ocorrencia < n:
		return -1
	else:
		return ocorrencias