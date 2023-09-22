def posLetra(string, letra, ocorrencia):
    '''dadas uma string, uma letra e a sua ocorrencia, retorna em que posiçao da string aquela ocorrencia está.
       caso exista menos ocorrencias do que a pedida, a função deve retornar -1
       : str, str, int -> int
    '''
    i = 0 
    n_ocorrencia = 0
    ocorrencias_total = string.count(letra)
    while n_ocorrencia < ocorrencia:
        if ocorrencias_total < ocorrencia:
            return -1
	    if string[i] == letra:
	        n_ocorrencia = n_ocorrencia + 1
        i = i + 1
	return i - 1