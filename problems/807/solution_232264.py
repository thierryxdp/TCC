def conta_frases (frase):
    ponto_final = frase.count(".")
    exclamacao = frase.count("!")
    interrogacao = frase.count("?")
    if "..." in frase:
		x = frase.count("...")
        correcao = (2 * x)
        return ponto_final + exclamacao + interrogacao - correcao
    else: 
        return ponto_final + exclamacao + interrogacao