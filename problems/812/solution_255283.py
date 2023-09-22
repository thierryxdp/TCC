def retira_pontuacao(frase):
    """Retorna a frase sem pontuacao.str-->str."""
    a=str.replace(frase,"!"," ")
	b=str.replace(a,":"," ")
	c=str.replace(b,";"," ")
	d=str.replace(c,"?"," ")
	e=str.replace(d,"."," ")
	f=str.replace(e,"-"," ")
    return f