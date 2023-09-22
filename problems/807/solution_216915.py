def conta_frases(texto):
	'''conta a quantidade de frases no texto
    str -> tupla'''
    x = texto.count("...")
    x = texto.count(".")
    y = texto.count("!")
    w = texto.count("?")
    return x+y+w