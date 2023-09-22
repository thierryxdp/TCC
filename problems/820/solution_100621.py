def posLetra(frase, letra, posicao):
    frase = list(frase)
    pos = 0 # contador
    indices = [] # acumulador
    while pos < len(frase):
        if letra in frase[pos]:
            indices = indices + [pos]
        pos = pos + 1
    if len(indices) < posicao:
        return -1
    else:
    	return indices[2]