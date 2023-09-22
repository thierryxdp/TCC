def retira_pontuacao(frase):
    
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
    
    import re
    Remover = re.substitute(r'[^\w\s]','',frase)
	
    return Remover