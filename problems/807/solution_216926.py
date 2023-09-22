def conta_frases(texto):
	'''conta a quantidade de frases no texto
    str -> tupla'''
    Int = texto.count("?")
    Pont = texto.count(".")
    Exc = texto.count("!")
    Ret = texto.count("...")
    ret = texto.count("...")*3
    return (Int+Pont+Exc+Ret)-ret