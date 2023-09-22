def retira_pontuacao(frase):
   	for sim_pon in frase:
	 sim_pon=["'", ",", ".", "!", ":", ";"]
     frase=frase.replace("sim_pon", " ")
     return frase