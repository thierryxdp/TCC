def retira_pontuacao(frase):
	"""funcao que dada uma frase retorna a frase onde todos os caracteres de pontuacao tenham sido substituidos por espaco
    str -> str"""
    x=str.replace (frase,","," ")
    y=str.replace(x,"."," ")
    return y