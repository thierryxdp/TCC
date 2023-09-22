def posLetra(texto, letra, n):
	'''Retorna a posição da n-ésima ocorrência
    de uma letra na string;
    string, string (char), int -> int'''
    return [str(i) for i, char in enumerate(texto) if char == letra].index(str(n))