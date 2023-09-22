def retira_pontuacao(frase):
	"""Função que retira a pontuação, e retorna a substituição com espaço
    vazio.
    str->str"""
    f1=frase.replace("-", " ")
    f2=f1.replace(",", " ")
    f3=f2.replace(":", " ")
    f4=f3.replace(".", " ")
    f5=f4.replace("?", " ")
    f6=f5.replace("!", " ")
    
    return f6