def inverte(frase):
	s=str.split(frase," ")
	r=frase.reverse
	f=str.join(" ",frase)
	return f
   
def retira_ponruacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase