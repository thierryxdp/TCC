def retira_pontuacao(frase):
    """ Funcao que retorna uma frase sem as pontuacoes;
    	str -> str
    """
    pontuacoes = [',', ':', ';', '...', '.', '!', '?', '-']
    
    for pontuacao in pontuacoes:
        frase = frase.replace(pontuacao, ' ')
        
    return frase

def inverte(frase):
    """ Funcao que recebe uma frase como parametro retorna uma outra frase que contem as mesma palavras porem na ordem inversa e sem letras maiusculas;
    	str -> str
    """
    frase_formatada = str.lower(retira_pontuacao(frase))
    
    return " ".join(formatada.split(' ').reverse())