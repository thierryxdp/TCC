def retira_ponruacao(frase):
    d=[".",",","-",":",";"]
    for c in d:
        frase=str.replace(frase,c," ")
    return frase

def inverte(frase):
    f=list(frase)
    rf=list.sort(f,reverse=True)
	return rf