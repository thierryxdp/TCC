def conta_frases(texto):
#parametros: . - ! - ? - ...
	a = texto.count("!")
    b = texto.count("?")
    c = texto.count("...")
    d = texto.count(".")-3*c
    return a + b + c + d