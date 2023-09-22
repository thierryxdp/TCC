def retira_pontuacao(x):
  	new_string = x.translate({ord('-'):None})
	return(new_string)