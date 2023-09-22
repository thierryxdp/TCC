def conta_frases (texto):
    exclamacao=texto.count("!")
    interrogacao=texto.count("?")
    reticencias=texto.count("...")
    ponto=texto.count(".")
    pontuacao = ponto + reticencias + interrogacao + exclamacao
    if reticencias > 0:
        pontuacao += - reticencias*3
	return pontuacao