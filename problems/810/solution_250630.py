def inverte(frase):
    frase = retira_pontucao
	s=str.split(frase," ")
	s.reverse()
	f=str.join(" ",s)
	return f
   
def retira_ponruacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase