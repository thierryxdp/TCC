def conta_frases(frase):
	if("..." in frase):
		return str.count(frase,'...')+str.count(frase,"!")+str.count(frase,"?")+str.count(frase,".")
    if("." in frase):
        return str.count(frase,'.')
    return 0