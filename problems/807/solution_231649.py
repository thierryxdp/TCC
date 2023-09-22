def conta_frases(texto):
	texto_1=texto.split(".")
	texto_2=texto.split("!")
	texto_3=texto.split("?")
	texto_geral=(texto_1,texto_2,texto_3)
	return len(texto_geral)