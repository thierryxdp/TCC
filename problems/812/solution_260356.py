def retira_pontuacao(frase):
    '''Dada uma frase, retorna uma frase onde
    todos os caracteres de pontuacao tenham 
    sido substituidos por espaco'''
 	
    sem_ponto = str.replace(frase,'.',' ')
 	return sem_ponto