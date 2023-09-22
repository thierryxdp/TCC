def posLetra(string, letra, pos):
    """A funçaõ retorna em que posiçao a string está em
	uma ocorrência dada;
	str, str, int -> int"""
    i = 0
    j = 0
    while i < len(string) and j < pos:
        if string[i] == letra:
        	j+=1
        i+=1
    if j < pos:
        return -1
    else:
    	return i-1