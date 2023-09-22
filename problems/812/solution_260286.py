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