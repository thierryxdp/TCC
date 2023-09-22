def retira_pontuacao(texto):
    if "-" in texto:
        texto=texto.replace("-"," ")
        return texto
	elif "," in texto:
        texto=texto.replace(","," ")
        return texto