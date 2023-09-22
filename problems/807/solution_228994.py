def conta_frases(frases):
	return len(list(filter(lambda x: len(x) > 0, frases.replace("!", "...").replace("?", "...").replace("...", ".").strip().split("."))))