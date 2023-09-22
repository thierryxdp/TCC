def retira_pontuacao(frase):
    '''retorna uma frase onde todos os caracteres de pontuação são substituídos por
    	espaço.
        str -> str'''
    
    
	condicao = '!' in 'frase'
    if condicao == True:
        return str.replace(frase, "!", " ")