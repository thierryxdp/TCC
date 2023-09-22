def retira_pontuacao(frase)
	a=frase.replace("-"," ")
    b=a.replace(","," ")
    c=b.replace(":"," ")
    d=c.replace(";"," ")
    e=d.replace("."," ")
    return e