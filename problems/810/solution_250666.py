def inverte(frase):
    frase=retira_pontuacao(frase)
	s=str.split(frase," ")
	s.reverse()
	f=str.join(" ",s)
	m=str.lower(f)
    return m

   
def retira_pontuacao(frase):
    d=[".",",",":",";"]
    for c in d:
        frase=str.replace(frase,c,"")
    return frase