def conta_frases(texto):
	'''conta a quantidade de frases no texto
    str -> tupla'''
    Nint = texto.count("?")
    Npont = texto.count(".")
    Nexc = texto.count("!")
    Nret = texto.count("...")
    Nreti = texto.count("...")*3
    return (Nint+Npont+Nexc+Nret)-Nreti