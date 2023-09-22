def posLetra(frase, letra, n):
    """Recebe uma string, uma letra e o numero de ocorrencia e retorna
    a posição da string em que àquela ocorrência da letra occore;
    str, str, int -> int"""
    pos = -1
    if n <= frase.count(letra):
        indice_anterior = 0
        i = 0
    	while i < n:
            indice_anterior = frase.find(letra, indice_anterior)
            indice_anterior += 1
        	i += 1
        pos = indice_anterior
    return pos