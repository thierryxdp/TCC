def retira_pontuacao(frase):
    """Retorna a frase sem pontuacao.str-->str."""
    a=str.replace(frase,"!"," ")
	b= str.replace(frase,":"," ")
	c= str.replace(frase,";"," ")
	d= str.replace(frase,"?"," ")
	e= str.replace(frase,"."," ")
	f= str.replace(frase,"-"," ")
    return a+b+c+d+e+f