def retira_pontuacao(txt):
"""função que substitui pontuação por espaço"""
	troca = str.replace(txt,","," ")
    troca_2 = str.replace(troca,"."," ")
    troca_3 = str.replace(troca_2,"-"," ")
    troca_4 = str.replace(troca_3,"?"," ")
    troca_5 = str.replace(troca_4,"!"," ")
    
	return troca_5