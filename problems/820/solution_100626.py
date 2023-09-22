def posLetra(frase, letra, ocorrencia):
    '''ao receber uma frase, uma letra e a ocorrência
    desejada da letra, retorna o índice onde a ocorrencia
    indicada se encontra na frase.
    str, str, int -> int'''
    frase = list(frase)
    pos = 0 # contador
    indices = [] # acumulador
    while pos < len(frase):
        if letra in frase[pos]:
            indices = indices + [pos]
        pos = pos + 1
    if len(indices) < ocorrencia:
        return -1
    else:
    	return indices[ocorrencia-1]