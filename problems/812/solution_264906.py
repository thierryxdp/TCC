def retira_pontuacao(frase):
    '''
    
    '''
    tipos_pontuacoes = ['-', ',', ':', ';', '.', '!', '?']
   
	if pontuacao in tipos_pontuacoes:
        frase = frase.replace(pontuacao, ' ')
        return frase