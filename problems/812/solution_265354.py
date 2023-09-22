def retira_pontuacao(frase):
    if str() in frase:
    	return str.replace(frase,","," ") and str.replace(frase,"."," ")