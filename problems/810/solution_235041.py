def retira_pontuacao (frase):
    '''Função substitui todas as pontuações por espaço.
    str -> str'''
    pontofinal = str.replace (frase, '.', ' ')
    exclamacao = str.replace (pontofinal, '!', ' ')
    interrogacao = str.replace (exclamacao, '?', ' ')
    travessao = str.replace (interrogacao, '-', ' ')
    virgula = str.replace (travessao, ',',' ')
    doispontos = str.replace (virgula, ':', ' ')
    pontovirgula = str.replace (doispontos, ';', ' ')
    return pontovirgula

def inverte (frase):
    '''Função inverte a ordem das palavras da frase (de tras pra frente), sem letras maiusculas e sem pontuação.
    str - > str'''
    fraseminuscula = str.lower (frase)
	frasenova = retira_pontuacao (fraseminuscula)
	listapalavra = str.split (frasenova)
	invertida = listapalavra [::-1]
	return str.join (' ', inverter)