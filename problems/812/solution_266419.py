def retira_pontuacao(entrada):
    separador = ['.','…','!','?','-',',',':',';']


	for j in separador:
    	entrada = entrada.replace(j, ' ')
    return entrada