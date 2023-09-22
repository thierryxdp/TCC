def retira_pontuacao(frase):
    """retira a pontuação de uma frase"""
    pontuacoes=[".",",","-",":",";","!","?"]
    frase=list(frase)
    s=""
    for x in frase:
        if x not in pontuacoes:
            s+=x
        else:
            s+=" "
	return s

def inverte(frase)
	frase=retira_pontuacao(frase)
    l=frase.split(" ")
    l=l.reverse()
    s=""
    for x in l:
        s+=x
        
	return s