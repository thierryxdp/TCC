def retira_pontuacao(frase):
    '''Dada uma frase, retorna uma frase onde
    todos os caracteres de pontuacao tenham 
    sido substituidos por espaco'''
    
    semponto = str.replace(frase,'.',' ')
    semvirgula = str.replace(str.replace(frase,'.',' '),',',' ')
	return semvirgula