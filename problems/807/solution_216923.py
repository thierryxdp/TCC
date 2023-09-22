def conta_frases(texto):
	'''conta a quantidade de frases no texto
    str -> tupla'''
    a = texto.count("?")
    b = texto.count(".")
    c = texto.count("!")
    d = texto.count("...")
    e = texto.count("...")*3
    return (a+b+c+d)-e