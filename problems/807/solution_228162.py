def conta_frases(frase):
     contagem = 0
    for char in frase:
    	if char == "!" or char == "?" or char == "..." or char == ".":
            contagem += 1
    return contagem