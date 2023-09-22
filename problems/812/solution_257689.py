def retira_pontiacao(frase):
    """ Funcao que retorna uma frase sem as pontuacoes;
    	str -> str
    """
    pontuacoes = [',', ':', ';', '...', '.', '!', '?']
    
    for pontuacao in pontuacoes:
        frase = frase.replace(pontuacao, ' ')
        
    return frase