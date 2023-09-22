def posLetra(texto, letra, n):
	'''Retorna a posição da n-ésima ocorrência
    de uma letra na string;
    string, string (char), int -> int'''
    listaOcorrencias = [str(i) for i, char in enumerate(texto) if char == letra]
    if len(listaOcorrencias) < n:
        return -1
    return listaOcorrencias[n - 1]