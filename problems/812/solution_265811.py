def retira_pontuacao(txt):
	troca = str.replace(txt,","," ")
    troca_2 = str.replace(troca,"-"," ")
    
	return troca_2