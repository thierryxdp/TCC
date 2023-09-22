def conta_frases(frases):
	return frases.replace("!", "...").replace("?", "...").replace("...", ".").strip().split(".")