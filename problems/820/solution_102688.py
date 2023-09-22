def posLetra(string, letra, n):
    '''Retorna o índice da ocorrência de letra pela nésima vez
    	str, str, int -> int'''
    i = 0
    ocorrencia = 0
    while i < len(frase):
        while ocorrencia < n:
        if string[i] == letra:
            ocorrencia = ocorrencia + 1
    return i