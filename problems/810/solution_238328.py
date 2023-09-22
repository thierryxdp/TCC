def retira_pontuacao(frase):
    """ Funcao que retorna uma frase sem as pontuacoes;
    	str -> str
    """
    pontuacoes = [',', ':', ';', '...', '.', '!', '?', '-']
    
    for pontuacao in pontuacoes:
        if pontuacao != '-':
            frase = frase.replace(pontuacao, '')
        else:
            frase = frase.replace(pontuacao, ' ')
        
    return frase

def inverte(frase):
    """ Funcao que recebe uma frase como parametro retorna uma outra frase que contem as mesma palavras porem na ordem inversa e sem letras maiusculas;
    	str -> str
    """
    frase_formatada = str.lower(retira_pontuacao(frase))
    frase_formatada = frase_formatada.split(' ')
    frase_formatada.reverse()
    return " ".join(frase_formatada)