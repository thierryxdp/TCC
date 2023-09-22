def inverte(frase):
    retira_pontuacao(frase)=frase
	s=str.split(frase," ")
	s.reverse()
	f=str.join(" ",s)
	return f
   
def retira_pontuacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase