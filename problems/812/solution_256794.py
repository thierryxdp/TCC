def retira_pontuacao(frase):
    import re
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
    Remover = re.sub(r'[^\w\s]','',frase)
	
    return Remover