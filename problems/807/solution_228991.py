def conta_frases(frases):
	return len(frases.replace("!", "...").replace("?", "...").replace("...", ".").strip().split("."))