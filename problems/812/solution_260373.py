def retira_pontuacao(frase):
    '''Dada uma frase, retorna uma frase onde
    todos os caracteres de pontuacao tenham 
    sido substituidos por espaco'''
    
    sempontovirgula = str.replace(str.replace(frase,'.',' '),',',' ')
	seminterrogacaotravessao = str.replace(str.replace(sempontovirgula,'?',' '),'-',' ')
    
    return seminterrogacaotravessao