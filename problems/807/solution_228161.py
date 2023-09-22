def conta_frases(frase):
    i = contagem
    for char in frase:
    	if char == "!" or char == "?" or char == "..." or char == ".":
            i += 1
    return i