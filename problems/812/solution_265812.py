def retira_pontuacao(txt):
	troca = str.replace(txt,","," ")
    troca_2 = str.replace(troca,"-"," ")
    troca_3 = str.replace(troca_2,"."," ")
    
	return troca_2