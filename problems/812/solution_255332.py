def retira_pontuacao(frase):
    """Retorna a frase sem pontuacao."""
    a=str.replace(frase,"!"," ")
    b=str.replace(a,"?"," ")
    c=str.replace(b,";"," ")
	d=str.replace(c,":"," ")
	e=str.replace(d,"."," ")
	f=str.replace(e,","," ")
    g=str.replace(f,"-"," ")
    return g