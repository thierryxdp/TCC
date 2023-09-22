def retira_pontuacao(frase):
    ''' funcao que retira a pontuação da frase. str->str'''
	a=frase.replace("-"," ")
    b=a.replace(","," ")
    c=b.replace(":"," ")
    d=c.replace(";"," ")
    e=d.replace("."," ")
    f=e.replace("!"," ")
    g=f.replace("?"," ")
    return g