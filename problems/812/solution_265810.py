def retira_pontuacao(txt):
	troca = str.replace(txt,","," ")
    troca_2 = str.replace(troca,"_"," ")
    
	return troca_2