def conta_frases(frase):
	str.replace(frase,".","-")
    
	return str.count(frase,"...")+str.count(frase,"!")+str.count(frase,"?")+str.count(frase,"-")