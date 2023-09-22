def retira_pontuacao(frase):
    '''Dada uma frase, retorna uma frase onde
    todos os caracteres de pontuacao tenham 
    sido substituidos por espaco'''
    
    sempontovirgula = str.replace(str.replace(frase,'.',' '),',',' ')
	seminterrogacaotravessao = str.replace(str.replace(sempontovirgula,'?',' '),'-',' ')
    frasefinal = str.replace(seminterrogacaotravessao,'!',' ')
    return frasefinal

def inverte(frase):
	'''Dada uma frase, retorna uma outra frase com as 
    palavras em ordem inversa e sem pontuacao
    str -> str'''
    
    
    palavras = str.split(str.lower(retira_pontuacao(frase)))
    invertido = list.reverse(palavras)
    frasenova = str.join(' ',str(invertido))
    return frasenova