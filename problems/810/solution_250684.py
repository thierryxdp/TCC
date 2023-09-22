def inverte(frase):
    frase=retira_pontuacao(frase)
	frase=str.split(frase)
	frase.reverse()
	frase=str.join(" ",frase)
	frase=str.lower(frase)
    return str.strip(frase)

   
def retira_pontuacao(frase):
    d=[".",",",":",";","-","!","?"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase