def retira_pontuacao(frase):
	"""funcao que recebe uma frase e retorna a mesma só que substituindo as pontuações por espaço
	str -> str"""
    
    ponto = str.replace(frase, '.', ' ')
    virgula = str.replace(ponto, ',', ' ')
    travessao = str.replace(virgula, '-', ' ')
    doispontos = str.replace(travessao, ':', ' ')
    pontovirgula = str.replace(doispontos, ';', ' ')
    exclamacao = str.replace(pontovirgula, '!', ' ')
    interrogacao = str.replace(exclamacao, '?', ' ')
    
    return interrogacao


def inverte(frase1):
    """funcao que recebe uma frase, e retorna a mesma só que sem pontuação, minuscula, e invertida
	str -> str"""
    
    frase2 = retira_pontuacao(frase1)
    frase3 = str.lower(frase2)
    split = str.split(frase3, ' ')
    inverte = split[::-1]
    junta = str.join(' ', inverte)
    
    return junta