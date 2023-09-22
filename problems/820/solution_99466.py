def posLetra(texto,l,n):
    """ """
    if str.count(texto,l) < n:
        return -1
    vzs = 0
    while vzs != n:
        resposta = 0
        resposta += str.find (texto,l)
        vzs += 1
        texto = texto[resposta:]
	return resposta