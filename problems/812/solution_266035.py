def retira_pontuacao(frase):
   	sim_pon in frase
	sim_pon=["'", ",", ".", "!", ":", ";"]
    frase=frase.replace("sim_pon", " ")
    return frase