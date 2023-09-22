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
    
    removeponto = retira_pontuacao(frase1)
    minuscula = str.lower(removeponto)
    split = str.split(minuscula)
    inverte = split[::-1]
    junta = str.join(' ', inverte)
    
    return junta