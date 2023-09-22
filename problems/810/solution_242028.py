def retira_pontuacao(frase):
    pontuacoes=[".",",","-",":",";","!","?"]
    frase=list(frase)
    s=""
    for x in frase:
        if x not in pontuacoes:
            s+=x
        else:
            s+=" "
	return s

def inverte(s):
	frase=retira_pontuacao(s)
	frase=frase.lower()
    l=frase.split(" ")
    l.reverse()
    a=""
    for x in l:
        if x!=" "
        	a+=x+" "
        
    return a