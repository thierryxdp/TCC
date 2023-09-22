def retira_pontuacao(frase):
    '''retorna uma frase onde todos os caracteres de pontuação são substituídos por
    	espaço.
        str -> str'''
    
    if '!' in 'frase':
        return str.replace(frase, "!", " ")