def inverte(frase):
    frase=retira_pontuacao(frase)
	frase=str.split(frase," ")
	s.reverse()
	frase=str.join(" ",frase)
	frase=str.lower(frase)
    return frase

   
def retira_pontuacao(frase):
    d=[".","-",",",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase