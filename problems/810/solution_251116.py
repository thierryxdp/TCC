def retira_pontuacao(txt):
	"""função que substitui pontuação por espaço
str -> str"""
	troca = str.replace(txt,","," ")
    troca_2 = str.replace(troca,"."," ")
    troca_3 = str.replace(troca_2,"-"," ")
    troca_4 = str.replace(troca_3,"?"," ")
    troca_5 = str.replace(troca_4,"!"," ")
    
def inverte(troca_5):
    return troca_5