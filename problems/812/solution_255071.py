def retira_pontucao(frase):
	"""Retorna a frase dada sem pontuação string -> string"""
	str.replace(frase,"-"," ")
	str.replace(frase,","," ")
	str.replace(frase,":"," ")
	str.replace(frase,";"," ")
	str.replace(frase,"..."," ")
	str.replace(frase,"!"," ")
	str.replace(frase,"?"," ")
	return frase