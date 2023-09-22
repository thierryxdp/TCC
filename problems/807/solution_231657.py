def conta_frases(texto):
	texto_1=texto.split(".")
	texto_2= list.extend(texto_1,"!")
	texto_3= list.extend(texto_2,"?")
	return len(texto_3)