def posLetra(stringue,letra,numero):
	"""retorna a posicao da string q a ocorrencia da letra ta, caso exita menos ocorrencias retorna -1"""
    if str.count(stringue,letra)<numero:
        return -1