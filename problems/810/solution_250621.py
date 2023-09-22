def inverte(frase):
	s=str.split(frase," ")
	r=s.reverse
	f=str.join(" ",r)
	return f
   
def retira_ponruacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase