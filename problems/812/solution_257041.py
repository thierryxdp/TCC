def retira_pontuacao(frase):
	"""funcao que dada uma frase retorna a frase onde todos os caracteres de pontuacao tenham sido substituidos por espaco
    str -> str"""
    a=str.replace (frase,","," ")
    b=str.replace(a,"."," ")
    c=str.replace(b,"!"," ")
    d=str.replace(c,"?"," ")
    e=str.replace(d,"-"," ")
    f=str.replace(e,":"," ")
    g=str.replace(f,";"," ")
    return g