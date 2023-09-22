posLetra (texto,l,n):
    """ """
    vzs = 0
    if str.count(texto,l) < n:
        return -1
    while vzs != n:
        resposta = 0
        resposta += str.find (texto,l)
        vzs += 1
        texto = texto[resposta:]
	return resposta