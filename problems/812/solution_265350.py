def retira_pontuacao(frase):
    if "." or "," in frase:
    	return str.replace(frase,","," ") and return str.replace(frase,"."," ")