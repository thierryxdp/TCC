def posLetra(frase,letra,ocorrencia):
    'retorna a posição em numero de uma determinada ocorrencia'
    'de um valor dentro de uma string, se tiver menos ocorrencias
    'que o solicitado vai ser retornado -1'
	'str,srt,int->int'
    i = 0
    n = 0
    while i<len(frase) and n<ocorrencia:
        if frase[i] == letra:
            n = n +1
        i = i + 1
    if n < ocorrencia:
        return -1
    else:
        return i-1